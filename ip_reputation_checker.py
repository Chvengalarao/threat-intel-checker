malicious_ips = {
    "45.77.21.10": {"country": "Russia", "risk": "High"},
    "185.234.72.10": {"country": "China", "risk": "High"},
    "103.45.67.89": {"country": "Unknown", "risk": "Medium"}
}

ip = input("Enter IP address: ")

print("\n=== Threat Intelligence Report ===")

if ip in malicious_ips:
    print("IP:", ip)
    print("Status: Malicious")
    print("Country:", malicious_ips[ip]["country"])
    print("Risk Score:", malicious_ips[ip]["risk"])
else:
    print("IP:", ip)
    print("Status: Not found in threat database")
