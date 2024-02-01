#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# intall nginx if it is not allready
apt-get update
apt-get install -y nginx

# creating folders 
mkdir -p /data/ /data/web_static /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test

# crating index file with hi
echo "<h1>HI</h1>" > /data/web_static/releases/test/index.html

# crating the link
ln -sf /data/web_static/releases/test/ /data/web_static/current


# chaningg owner and groub
chown -R ubuntu:ubuntu /data

# editing the config if not exists
ok=$(< /etc/nginx/sites-available/default tr ' ' _ | grep hbnb_static | wc -c)

if [ "$ok" == "0" ]; then

        sed -i "/server_name/a\
        \\
        location \/hbnb_static\/ {\n\
                alias \/data\/web_static\/current\/;\n\
        }
        " /etc/nginx/sites-available/default
fi

# restart
service nginx restart
