malicious_ips = {
    "45.77.21.10": {"country": "Russia", "risk": "High"},
    "185.234.72.10": {"country": "China", "risk": "High"},
    "103.45.67.89": {"country": "Unknown", "risk": "Medium"}
}

print("=== Threat Intelligence IP Checker ===")

ip = input("Enter IP address: ")

print("\nThreat Intelligence Report")
print("---------------------------")

if ip in malicious_ips:
    print("IP Address :", ip)
    print("Status     : Malicious")
    print("Country    :", malicious_ips[ip]["country"])
    print("Risk Level :", malicious_ips[ip]["risk"])
else:
    print("IP Address :", ip)
    print("Status     : No threat intelligence found")
