# 💀Track-Them💀

## 📜Description
Track-Them is a fully automated IP tracking tool designed for ethical use.  
It logs visitor details in real-time, saves them, and provides a masked tracking link that redirects users  
to any desired URL. It features a live dashboard, auto-installs Cloudflare Tunnel, and ensures a seamless  
experience with just one click.  

## 🔑Features
- ✔ One-click tracking – Fully automated setup and execution.  
- ✔ Masked URL – Generates a clean tracking link.  
- ✔ Real-time logging – Shows visitor details in the terminal and saves them to a file.  
- ✔ Live dashboard – Web-based panel to monitor logs dynamically.  
- ✔ Auto Tunnel Setup – Supports Cloudflare Tunnel (Serveo/Ngrok can be added).  
- ✔ Cross-platform – Works on Linux, Mac, and Windows (WSL).  
- ✔ Geolocation tracking – Fetches country, city, ISP, and other details.  

## 🚀Step-by-Step Guide in Linux Terminal !

Step 1: Update & upgrade your system  
>sudo apt update  

>sudo apt upgrade  

Step 2: install Dependencies  
>sudo apt install python3-flask  

>sudo apt install python3-requests  

Step 3: Clone the repository  
>git clone https://github.com/The-Real-Virus/Track-Them.git  

Step 4: Go to the Tool Directory where u clone it  
>cd Track-Them  

Step 5: After Completing the process now u can run script  
>python3 tracker.py  

## 💡Tips !
🌐 Must Use a URL shortener to make the tracking link look natural.  
⚡ Recommended URL shortners : (https://bitly.com/) , (https://grabify.link/) , (https://t.ly/) .  
✅ Tracking link generated: "Send this link to victim".  
📊 View real-time logs: "Use this link in ur own browser to see dashboard".  
🔄 Refresh /dashboard every few seconds for real-time logs.  
🛑 Use this responsibly – only on your own systems or with permission.  
⚡ Always check the tracking link in ur own browser first before sending to someone, make sure it is working.  
📊 Cloudflare links refresh some times , re run the script then.  
🔄 You can share one link to multiple victims.  
🔄 it will download cloudflare only on first run if not already install.  

## 🤝Follow the Prompts !
1) This script is fully interactive! Just:  
2) Run it:  
3) Follow the on-screen instructions.  
4) Share the generated link and track in real time!  

## ⚙️Troubleshooting

1) `Issue: Flask Not Found?:`  
- install the requirements (step 2 above).  

2) `Issue: Cloudflare link Not Working?:`  
- its due to cloudflare server down sometimes, run script after few time maybe hours...  

3) `Issue: Permission Denied?:`  
- try this command (chmod +x tracker.py), then run script.  

4) `Issue: Python3 or pip not found?:`  
- read the requirements.txt file, (cat Requirements.txt) or (gedit Requirements.txt).  

## 🛠️MODIFICATION 

IF U WANT TO MODIFY OR USE THE SCRIPT IN UR PROJECTs , CONSIDER GIVING CREDITS !  

## 📂Example OutPut

	Terminal Log:

	[🔍 Visitor Logged]
	Time:       2025-03-13 12:30:45
	IP:         192.168.1.100
	City:       New York
	Region:     NY
	Country:    USA
	Latitude:   40.7128
	Longitude:  -74.0060
	ISP:        Verizon Communications
	Timezone:   America/New_York
	User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
	----------------------------------------

	Real-Time Dashboard Preview:

	| Time             | IP             | Location           | ISP                    | User-Agent             |  
	|------------------|----------------|--------------------|------------------------|------------------------|  
	| 2025-03-13 12:30 | 192.168.1.100  | New York, NY, USA  | Verizon Communications | Mozilla/5.0 (Windows)  |  
	| 2025-03-13 12:35 | 203.0.113.45   | London, UK         | British Telecom        | Chrome/100.0.1         |  

	----------------------------------------

# ⚠️Disclaimer !
This tool is intended for ethical and educational use only.  
Do not use it for illegal activities. The author is not responsible for any misuse.  
This script is intended for educational purposes and authorized testing only.  
Unauthorized use of this script is illegal and unethical.  
Ensure you have explicit permission before testing any system.  
- Obtain explicit permission before testing any system.  
- Adhere to all applicable laws and regulations.  
- Respect user privacy and data.  
- By using this script, you agree to take full responsibility for your actions.  
