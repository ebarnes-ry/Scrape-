#!/bin/bash

#This Bash Scripts are to run inside the server 20.0.2.117 this will triger the VPN change ip address

sudo openvpn --config /etc/openvpn/configs/ipvanish-US-Atlanta-atl-a02.ovpn --auth-user-pass /etc/openvpn/password.txt &

bash /home/ubuntu/timer.sh &&

echo "OVPN tunneling success" > /home/administrator/adultresearch/log_adult.txt &&

python3 /home/administrator/adultresearch/scrape_adult_alpha_2.py 

echo "File created sucess" >> /home/administrator/adultresearch/log_adult.txt &&

sudo killall openvpn &&

echo "kill vpn connection success" >> /home/administrator/adultresearch/log_adult.txt
