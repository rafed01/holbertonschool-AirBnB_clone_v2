#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
sudo apt-get update
sudo apt-get install nginx -y nginx

# Create the folders
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/

# Create a fake HTML file
    echo "<!DOCTYPE html>
    <html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
    </html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the folder
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to server
sudo sed -i '48i \\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
