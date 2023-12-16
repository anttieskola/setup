# Network manager
Notes about it

Configuration found in `/etc/NetworkManager/`
Current status in `/var/lib/NetworkManager/`

## Device list
```bash
nmcli device
```

Example
```
DEVICE           TYPE      STATE                   CONNECTION
enx0c5b8f279a64  ethernet  connected               Usb4gModem
enp10s0          ethernet  connected               LAN
lo               loopback  connected (externally)  lo
```


### Device status
```bash
nmcli device show enp10s0
```

Example
```
GENERAL.DEVICE:                         enp10s0
GENERAL.TYPE:                           ethernet
GENERAL.HWADDR:                         04:42:1A:1F:34:18
GENERAL.MTU:                            1500
GENERAL.STATE:                          100 (connected)
GENERAL.CONNECTION:                     LAN
GENERAL.CON-PATH:                       /org/freedesktop/NetworkManager/ActiveConnection/3
WIRED-PROPERTIES.CARRIER:               on
IP4.ADDRESS[1]:                         192.168.2.30/24
IP4.GATEWAY:                            192.168.2.30
IP4.ROUTE[1]:                           dst = 0.0.0.0/0, nh = 192.168.2.30, mt = 101
IP4.ROUTE[2]:                           dst = 192.168.2.0/24, nh = 0.0.0.0, mt = 101
IP6.ADDRESS[1]:                         fe80::fbdd:2b21:5cb5:9d25/64
IP6.GATEWAY:                            --
IP6.ROUTE[1]:                           dst = fe80::/64, nh = ::, mt = 1024
```

## Restart network manager
```bash
sudo systemctl restart systemd-networkd
```