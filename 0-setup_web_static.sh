#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Hello World" | sudo tee /data/web_static/releases/test/index.html
sudo ln -f -s /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu /data/
sudo sed -i '20i\\tlocation /hbnb_static/{\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
