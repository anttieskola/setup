# Samba setup

Installation

```bash
sudo apt-get install samba
sudo ufw allow Samba
sudo ufw reload
```

Configuration is found in `/etc/samba/smb.conf`

The configuration is very well documented and is most likely enough to just read the template and configure there what you need. Remembet to run `testparm`command to check
configuration for errors.

Only thing to note is that each user has separate password for samba.
Just remember to set the separate password using the tool `smbpasswd` for the user you want to use to access the shares.

Adding user and enabling it

```bash
sudo smbpasswd -a antti
...
sudo smbpasswd -e antti
```

My simple setup with workgroup, restricted access (just from local network), couple read/write shares to authenticated users. Other than this I did disable login/logon stuff, guest access, home folder, profiles and printers.

This is now working somewhat, not sure why when I add `bind interfaces only` it breaks.
Not sure does subnetwork defition work in this options to do what I wanted which is restrict
allowed hosts into the range 192.168.1.1 - 62, but thats the purpose of it.

```ini
[global]                                     security = user
valid users = antti
server string = storage
map to guest = Bad User

# allow access from specific ip's
interfaces = 192.168.1.253 192.168.1.252 192.168.1.251 192.168.1.250 192.168.1.249

log file = /var/log/samba/log.%m
max log size = 1000
logging = file
panic action = /usr/share/samba/panic-action %d

[ares0]
path = /mnt/ares0
read only = no

```

Restarting service

```bash
sudo systemctl restart smbd
```
