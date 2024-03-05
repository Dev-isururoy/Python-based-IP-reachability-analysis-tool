import subprocess

def ping_ip(ip_address, device_name, packet_count=5, timeout=20):
    try:
        result = subprocess.run(['ping', '-n', str(packet_count), '-w', str(timeout * 1000), ip_address], capture_output=True, text=True, timeout=timeout)
        if f"Received = {packet_count}" in result.stdout:
            return f"Successfully pinged {device_name:<40} ({ip_address})"
        else:
            return f"Failed to ping {device_name:<40} ({ip_address})"
    except Exception as e:
        return f"Error while pinging {device_name:<40} ({ip_address}): {str(e)}"

def main():
    devices = [
        ("192.168.5.2", "Firewall"),
        ("192.168.10.1", "Core 01"),
        ("192.168.10.3", "Switch 01 Aruba POE"),
        ("192.168.10.4", "Switch 02 HP 01"),
        ("192.168.10.5", "Switch 03 HP 02"),
        ("192.168.10.6", "Switch 04 Service Floor"),
        ("192.168.10.7", "Switch 05 Service Floor"),
        ("192.168.10.8", "Switch 06 Engineering"),
        ("192.168.10.9", "Switch 07 Canteen"),
        ("192.168.10.10", "Switch 08 Power House"),
        ("192.168.10.12", "Switch 10 Boiler Site"),
        ("192.168.10.13", "Switch 11 Locker Room"),
        ("192.168.50.250", "NVR 01"),
        ("192.168.50.251", "NVR 02"),
        ("192.168.30.233", "Primary Domain Server"),
        ("192.168.30.190", "Secondary Domain Server"),
        ("192.168.30.234", "HRM Server"),
        ("192.168.30.232", "Domain Server (NAS)"),
        ("192.168.20.200", "BMS Server"),
        ("192.168.30.199", "NTP Server"),
        ("192.168.40.250", "WIFI NVR"),
        ("192.168.70.100", "Locker Room Fingerprint Machine"),
        ("192.168.70.28", "Server Room Fingerprint Machine"),
        ("192.168.30.191", "Production Office Printer"),
        ("192.168.30.195", "P&A Black & White Printer"),
        ("192.168.30.197", "Color Printer"),
        ("192.168.30.242", "Engineering Office"),
        ("192.168.30.196", "QC Black & White"),
        ("192.168.30.239", "QC color Printer (Smart Tank)"),
        ("192.168.30.170", "Mr. Parag Printer"),
        ("192.168.30.207", "QA Black & White Printer"),
        ("192.168.30.189", "QA Color Printer"),
        ("192.168.30.114", "QA Color Printer (Smart Tank)"),
    ]

    company_name = "Kelun LifeSciences Pvt. Ltd."

    try:
        for ip_address, device_name in devices:
            result = ping_ip(ip_address, device_name)
            print(result)
    except KeyboardInterrupt:
        print("\nPing stopped by user")

    print(f"\nPing test for {company_name} completed.")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
