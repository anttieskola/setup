- [nftables-wiki](https://wiki.nftables.org/wiki-nftables/index.php/Main_Page)
- [nftables-debian](https://wiki.debian.org/nftables)


# UFW - Uncomplicated Firewall
```bash
sudo apt install ufw

# sudo ufw allow <port number>/<optional protocol>

# example of pihole
sudo ufw allow ssh
sudo ufw allow dns
sudo ufw allow http
sudo ufw allow https

# then just enable (right away + systemd)
sudo ufw enable

# if you must disable
sudo ufw disable
````

## TCP
- 22 ssh
- 80 http
- 443 https
- 5432 postgresql
- 18080 monero
