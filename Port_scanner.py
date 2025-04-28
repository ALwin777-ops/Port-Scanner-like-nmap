import pyfiglet
import socket 
import sys
from datetime import datetime

banner = pyfiglet.figlet_format("PORT SCANNER LIKE NMAP")
print(banner)

target = input(str("Enter The Target (e.g., 7.7.3.8 or example.com): "))

print("_" * 50)
print(f"Scanning Target: {target}")
print(f"Scanning Started at: {datetime.now()}")
print("_" * 50)

try:
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Set timeout on the socket, not on the module
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is Open")
        s.close()
except KeyboardInterrupt:
    print("\n[!] Exiting Program...")
    sys.exit()
except socket.gaierror:
    print("[!] Hostname Could Not Be Resolved. Exiting")
    sys.exit()
except socket.error:
    print("[!] Server Not Responding. Exiting")
    sys.exit()
