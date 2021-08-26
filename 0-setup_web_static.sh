#!/usr/bin/env bash
#sets up the web server for the deployment of web_static

apt-get update
apt-get install nginx -y

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/
ln -sf /data/web_static/releases/test/ /data/web_static/current

echo "<html>
  <head>
  </head>
  <body>
    Peppa Pig
  </body>
</html>" > /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /var/www/html/index.html

printf %s "server {
    listen 80;
    listen [::]:80;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html;
    location /hbnb_static/ {
        alias /data/web_static/current;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
