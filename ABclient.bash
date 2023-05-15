#!/bin/bash
git clone https://github.com/amchp/TET-proyecto-2.git
cd TET-proyecto-2
sudo sh dockersetup.sh
cd client
PUBLIC_IP=$(ec2metadata --public-ipv4)
PRIVATE_IP=$(ec2metadata --local-ipv4)
INSTANCE_ID=$(ec2metadata --instance-id)
sudo docker compose build
sudo docker compose up
