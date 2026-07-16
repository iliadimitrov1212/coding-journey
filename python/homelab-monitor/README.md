# Homelab Status Monitor

A Python program that monitors whether machines in my VirtualBox Linux homelab are reachable.

## Version 1 — Command-Line Monitor

The original version runs manually from the terminal.

- Checks multiple machines using `ping`
- Reports each machine as online or offline
- Uses Python's `subprocess` module

## Version 2 — systemd Automation

The second version runs automatically using a systemd service and timer.

- Runs every minute
- Stores results in the systemd journal
- Starts automatically when `u1` boots
- Detects when a machine becomes unreachable

## Version 2.5 — Timestamped Monitoring

An update to Version 2 that adds the local date, time, and time zone to each status check.

Features:

- Displays when each monitoring check was performed
- Uses the virtual machine’s configured local time zone
- Makes systemd journal results easier to track
- Keeps the automatic service and timer from Version 2
  
## Version 3 — Web Dashboard

The planned third version will display machine status on a local webpage.
