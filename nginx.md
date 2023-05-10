# Nginx

## Installation
```bash
sudo apt install nginx-full
```

## Redirect http to https
Configure to the site (running only one site atm)

```
server {
        listen 80 default_server;
        server_name _;
        return 301 https://$host$request_uri;
}
```