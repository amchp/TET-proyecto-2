#!/bin/bash
cd /home/ubuntu/
git clone https://github.com/amchp/TET-proyecto-2.git
cd TET-proyecto-2
sudo sh dockersetup.sh
cd client
sudo set -e -x
sudo echo PUBLIC_IP=$(ec2metadata --public-ipv4) >> .env
sudo echo PRIVATE_IP=$(ec2metadata --local-ipv4) >> .env
sudo echo INSTANCE_ID=$(ec2metadata --instance-id) >> .env
sudo docker compose build
sudo docker compose up
