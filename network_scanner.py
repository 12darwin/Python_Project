from scapy.all import ARP, Ether, srp
from reportlab.pdfgen import canvas
from datetime import datetime
import pytz
import socket

def get_current_time():
    tz = pytz.timezone("Asia/Manila")
    return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

def scan_network(ip_range):
    print(f"[+] Scanning network: {ip_range}")
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=2, verbose=0)[0]
    devices = []

    for sent, received in result:
        ip = received.psrc
        mac = received.hwsrc
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"
        devices.append({
            "ip": ip,
            "mac": mac,
            "hostname": hostname
        })

    return devices

def generate_pdf(devices, filename="network_report.pdf"):
    c = canvas.Canvas(filename)
    c.setFont("Helvetica", 12)
    c.drawString(100, 800, f"Network Scan Report - {get_current_time()}")
    c.drawString(100, 780, "IP Address".ljust(20) + "MAC Address".ljust(20) + "Hostname")

    y = 760
    for dev in devices:
        line = f"{dev['ip'].ljust(20)} {dev['mac'].ljust(20)} {dev['hostname']}"
        c.drawString(100, y, line)
        y -= 20

    c.save()
    print(f"[+] PDF report saved as {filename}")

def generate_html(devices, filename="network_report.html"):
    with open(filename, "w") as f:
        f.write("<html><head><title>Network Report</title></head><body>")
        f.write(f"<h2>Network Scan Report - {get_current_time()}</h2>")
        f.write("<table border='1'><tr><th>IP Address</th><th>MAC Address</th><th>Hostname</th></tr>")
        for dev in devices:
            f.write(f"<tr><td>{dev['ip']}</td><td>{dev['mac']}</td><td>{dev['hostname']}</td></tr>")
        f.write("</table></body></html>")

    print(f"[+] HTML report saved as {filename}")

if __name__ == "__main__":
    subnet = input("Enter IP range to scan (e.g. 192.168.1.0/24): ")
    result = scan_network(subnet)
    
    if not result:
        print("[-] No devices found.")
    else:
        generate_pdf(result)
        generate_html(result)

