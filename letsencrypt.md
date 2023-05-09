# Let's Encrypt
[Homepage](https://letsencrypt.org/)

## Starting point
- Local server setup (ares) running nginx
    - Local Ip 192.168.1.2
- Router set to forward ports 80 & 443 from public ip to ares
    - Public Ip 85.134.126.174

## Goal
- Setup CA for one of my domains to router's public ip
- Setup / learn to use let's encrypt to have SSL certificate

# Test plain http
- Site opened using a proxy web site correctly
- Added domain DNS type:`A` record for name:`www` to point to public ip adress
    - Now site works with domain name

# Configure https Nginx (self signed)
Main configuration `/etc/nginx/nginx.conf`
- Disable gzip (configuration refers to some bug with ssl and gzip)

Creating self-signed test certificate
```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/oma-selfsigned.key -out /etc/ssl/certs/oma-selfsigned.crt
```

Create new file `/etc/nginx/snipplets/oma-selfsigned.conf`
```
# self-signed test cert
ssl_certificate /etc/ssl/certs/oma-selfsigned.crt;
ssl_certificate_key /etc/ssl/private/oma-selfsigned.key;
```

Configure ssl to default site configuration `/etc/nginx/sites-available/default`
```
listen 443 ssl default_server;
listen [::]:443 ssl default_server;
include snippets/oma-selfsigned.conf;
```

Restart
```bash
sudo service nginx restart
```

Now https should work :)

# Certbot
- [Certbot](https://certbot.eff.org/)

```bash
sudo apt install certbot
```

Requesting certificate manually
```bash
sudo certbot certonly --manual --preferred-challenges http
```
- Use full domain name (DNS not setup for wildcard)
- Create file with content as requested
- Make new configuration snippet for the certificate and take into use

Now https is valid :) For couple months if public ip won't change...

## Automatic renewal
- Todo
