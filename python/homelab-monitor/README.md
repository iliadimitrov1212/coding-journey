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

## Version 3 — Web Dashboard

The planned third version will display machine status on a local webpage.
