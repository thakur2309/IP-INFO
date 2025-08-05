import requests
import ipaddress
import os
import time

# Clear the screen before running
os.system('clear' if os.name == 'posix' else 'cls')

# Tool Header
print("\033[1;34m" + "="*50)
print("🔥 TOOL NAME : IP-INFO")
print("🎯 Created by Alok Thakur")
print("📺 YouTube: Firewall Breaker")
print("📚 For Educational Purpose Only")
print("="*50 + "\033[0m\n")

# Get IP from user
ip = input("\033[1;33mEnter IP address: \033[0m")

# Check if the IP is private
try:
    if ipaddress.ip_address(ip).is_private:
        print("\n\033[1;31m⚠️ This is a Private IP Address. Location cannot be publicly traced.\033[0m\n")
        exit()
except:
    print("\033[1;31m❌ Invalid IP Address\033[0m")
    exit()

# Send request to ipinfo.io API
response = requests.get(f"https://ipinfo.io/{ip}/json")
data = response.json()

# Extract location coordinates
location = data.get("loc", "").split(',')

# Print IP details
print(f"\n\033[1;32m📍 Location Details:\033[0m")
print(f"\033[1;36mIP Address: \033[0m{ip}")
print(f"\033[1;36mCountry: \033[0m{data.get('country', 'N/A')}")
print(f"\033[1;36mRegion: \033[0m{data.get('region', 'N/A')}")
print(f"\033[1;36mCity: \033[0m{data.get('city', 'N/A')}")
print(f"\033[1;36mPostal Code: \033[0m{data.get('postal', 'N/A')}")
print(f"\033[1;36mTime Zone: \033[0m{data.get('timezone', 'N/A')}")
print(f"\033[1;36mISP / Org: \033[0m{data.get('org', 'N/A')}")
print(f"\033[1;36mASN: \033[0m{data.get('asn', {}).get('asn', 'N/A') if 'asn' in data else 'N/A'}")
print(f"\033[1;36mLatitude/Longitude: \033[0m{location[0] if location else 'N/A'}, {location[1] if len(location) > 1 else 'N/A'}")

# VPN/Proxy detection (basic via hosting check)
hosting = data.get("hosting", False)
if hosting:
    print("\033[1;31mVPN/Proxy: Detected (Hosting IP)\033[0m")
else:
    print("\033[1;32mVPN/Proxy: Not Detected\033[0m")

# Google Maps Link for location
if len(location) == 2:
    maps_link = f"https://www.google.com/maps?q={location[0]},{location[1]}"
    print(f"\n\033[1;35m🔗 Google Maps Link: \033[0m{maps_link}")
else:
    print("\n\033[1;31m🔗 Google Maps Link: Not Available\033[0m")
