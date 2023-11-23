# Nginx

## Errors
```bash
# Check Nginx configuration syntax
sudo nginx -t

# Tail Nginx error logs
sudo tail -f /var/log/nginx/error.log
```

## Installation
```bash
sudo apt install nginx-full
# for simple authentication (htpasswd utility)
sudo apt install apache2-utils
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

## Gzip
Configured gzip compression for x-javascript and assembly in `nginx.conf`
```
##
        # Gzip Settings
        ##

        gzip on;
        gzip_vary on;
        gzip_proxied any;
        gzip_comp_level 6;
        gzip_buffers 16 8k;
        gzip_http_version 1.1;
        gzip_types text/plain text/css application/json application/javascript application/x-javascript text/xml application/wasm application/xml application/xml+rss text/javascript;
```
This reduces webassembly sizes up to half of original :)

## Basic auth
Configuration part if using simple passwd file:
```
location /ai/ {
                auth_basic "Restricted area, sorry.";
                auth_basic_user_file /etc/nginx/.htpasswd;
        }
```

Adding users from command line/creating file:
```bash
sudo htpasswd -c /etc/nginx/.htpasswd antti
```
