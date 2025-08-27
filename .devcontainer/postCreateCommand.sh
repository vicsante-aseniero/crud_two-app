#!/bin/sh
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y xdg-utils
sudo apt-get update && sudo apt-get install -y net-tools
sudo apt install python3-pip -y

echo "Installing needed package(s)....."
pip3 install -r ./requirements.txt

python3 --version
pip3 --version
protoc --version
dapr version
echo "Done version verifications and installing needed package(s)....."