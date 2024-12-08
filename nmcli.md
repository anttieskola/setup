# If debian defaults in use
- install network-manager
```bash
sudo apt install network-manager
```

- enable network-manager
```bash
sudo systemctl enable NetworkManager
sudo systemctl start NetworkManager
```

- comment everything in /etc/network/interfaces

# Add devices to network manager

## eth
```bash
sudo nmcli c mod "eth0" ipv4.address 192.168.1.10/24 ipv4.method manual
sudo nmcli c mod "eth0" ipv4.gateway 192.168.1.254
sudo nmcli c mod "eth0" ipv4.dns "192.168.1.1,9.9.9.9"
```

## loopback
```bash
sudo nmcli connection add type loopback ifname lo con-name "lo"
sudo nmcli connection modify "lo" connection.autoconnect yes
sudo nmcli connection up "lo"
```

```bash
sudo nmcli connection up "eth0"
# breaks ssh of course, as ip changes
```

# Rename device
```bash
sudo nmcli connection modify "Wired connection 1" connection.id "eth0"
sudo nmcli connection modify "Local" connection.id "lo"
```
