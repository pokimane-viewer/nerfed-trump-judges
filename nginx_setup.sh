#!/usr/bin/env bash
set -e

sudo apt install python3-venv

sudo apt update
sudo apt install -y nginx

sudo ln -s /etc/nginx/sites-available/WHATEVER_THE_FUCK /etc/nginx/sites-enabled/

sudo nginx -t
sudo systemctl reload nginx
sudo systemctl restart nginx