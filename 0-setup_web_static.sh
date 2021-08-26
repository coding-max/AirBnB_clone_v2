#!/usr/bin/env bash
#sets up the web server for the deployment of web_static

apt-get update
apt-get install nginx -y

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/
ln -sf /data/web_static/releases/test/ /data/web_static/current

echo "This shit it's working" > /data/web_static/releases/test/index.html
echo "Holberton School" > /var/www/html/index.html

printf %s "<!doctype html5>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>404 error</title>
</head>
<body>
    <!-- get out of here pastrana -->
    <img style=\"display: block; margin: auto; margin-top: 150px;\" src=\"https://images.squarespace-cdn.com/content/v1/51cdafc4e4b09eb676a64e68/1470175715831-NUJOMI6VW13ZNT1MI0VB/image-asset.jpeg?format=300w\" alt=\"Girl in a jacket\" height=\"300\">
    <h2 style=\"display: block; text-align: center; font-size: xx-large; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin-bottom: 0;\">404 PAGE NOT FOUND</h2>
    <h3 style=\"display: block; text-align: center; font-size: large; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin-top: 5px;\">Ceci n'est pas une page</h3>
</body>
</html>" > /var/www/html/404.html

printf %s "server {
    listen 80;
    listen [::]:80;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
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
