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

## Project Status

This project is complete at Version 2.5.

It began as a basic Python script and was expanded into an automated
systemd service with timestamped results. The current version accomplishes
the original goal of monitoring whether machines in my homelab are reachable.

## Possible Future Extension

A web dashboard may be added later if the homelab grows and a visual status
page becomes genuinely useful.

## Known Limitation

The current program requires each machine's hostname and IP address to be
entered manually in the `machines` dictionary. This approach may become
difficult to manage as I add more virtual machines.

In a future version, I would like the program to automatically discover
machines on the Host-Only network. I do not yet know the best way to implement
this, so I am leaving it as a possible future improvement.
