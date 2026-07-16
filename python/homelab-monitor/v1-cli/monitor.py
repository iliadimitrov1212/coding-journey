import subprocess
from datetime import datetime

machines = {
    "u2": "192.168.56.104",
    "r10-1": "192.168.56.101",
}


def is_online(ip_address):
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", ip_address],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return result.returncode == 0


timestamp = datetime.now().astimezone().strftime(
    "%Y-%m-%d %I:%M:%S %p %Z"
)

print(f"=== HOMELAB STATUS — {timestamp} ===")

for hostname, ip_address in machines.items():
    if is_online(ip_address):
        print(f"{hostname} ({ip_address}) is ONLINE")
    else:
        print(f"{hostname} ({ip_address}) is OFFLINE")
