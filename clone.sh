#!/bin/bash 

REPO_URL="https://github.com/Sameer362/CICD-project-assignment5.git"
REPO_DIR="/home/ubuntu/project-5"
WEBSITE_DIR="/var/www/index"

cd $REPO_DIR

#pulling particular repo
git pull  $REPO_URL

# Copy files to website directory
rsync -av --delete $REPO_DIR/ $WEBSITE_DIR/

sudo systemctl restart nginx

sudo systemctl status nginx
