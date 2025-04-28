# PORT SCANNER LIKE NMAP

## Description
A simple Python script that scans all 65,535 ports on a specified target (IP address or domain name).  
It mimics basic functionality similar to tools like Nmap, displaying open ports and providing real-time scan status.

---

## Features
- Scans the full range of TCP ports (1–65535).
- Displays a banner using `pyfiglet`.
- Shows scanning details, including target and start time.
- Identifies and displays open ports.
- Handles exceptions such as:
  - User interruption (Ctrl + C)
  - Hostname resolution errors
  - Server connection issues

---

## Requirements
- Python 3.x
- Python libraries:
  - `pyfiglet`
  
You can install the required library using:
```bash
pip install pyfiglet
```

---

## How to Use
1. Save the script (e.g., `port_scanner.py`).
2. Open a terminal and navigate to the script’s directory.
3. Run the script:
```bash
python port_scanner.py
```
4. When prompted, enter the target IP address or domain name.
5. View the list of open ports as they are found.

---

## Important Notes
- This script uses a timeout of 0.5 seconds per port to speed up scanning.
- Scanning **all** ports may take some time depending on network speed and target system.
- **Use this script responsibly** — only scan systems you have permission to scan.

---

## Disclaimer
This project is intended for educational purposes only.  
The developer is not responsible for any misuse of this tool.
