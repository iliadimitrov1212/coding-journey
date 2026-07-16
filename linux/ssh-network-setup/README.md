# SSH Network Setup

## Objective

Set up a Linux homelab using VirtualBox and configure secure communication between virtual machines using SSH.

## Environment

### Operating Systems

- Rocky Linux
- Ubuntu Server
- Ubuntu Desktop

### Software

- VirtualBox
- OpenSSH

## Tasks Completed

- Installed Rocky Linux
- Installed Ubuntu Server
- Installed Ubuntu Desktop
- Configured hostnames
- Installed and enabled the OpenSSH server
- Generated SSH key pairs
- Copied SSH public keys between virtual machines
- Connected to remote machines using SSH
- Configured static IP addresses
- Explored DHCP configuration
- Compared NAT and Bridged networking modes
- Learned the purpose of Host-Only adapters

## Challenges

### DHCP Issue

Both Ubuntu Server and Rocky Linux were unable to obtain DHCP leases after switching from static IP addressing.

### Troubleshooting Steps

- Verified Netplan configuration
- Tested DHCP on Ubuntu
- Tested DHCP on Rocky Linux
- Compared static and dynamic IP configurations
- Investigated VirtualBox network settings
- Determined the issue was likely related to the current network environment rather than the Linux configuration itself.
### Outcome

Both Ubuntu Server and Rocky Linux timed out while requesting DHCP leases through VirtualBox bridged networking. Because the issue occurred on both operating systems, it was unlikely to be specific to either Linux configuration.

The exact root cause was not confirmed. The evidence suggested an issue involving the bridged-network path on the host laptop, such as the selected physical adapter, the VirtualBox bridge driver, or the host Wi-Fi adapter's handling of virtual MAC addresses.

I changed the design to use two virtual network adapters:

- NAT for automatic internet access
- Host-Only networking for stable communication between the host and virtual machines


## Commands Used

```bash
ip addr
ip route
nmcli
hostnamectl
ssh
ssh-keygen
ssh-copy-id
systemctl
sudo nano /etc/netplan/00-installer-config.yaml
sudo netplan apply
networkctl status
```

## Skills Learned

- SSH key authentication
- Linux networking
- Static IP configuration
- DHCP
- VirtualBox networking
- Basic system administration
