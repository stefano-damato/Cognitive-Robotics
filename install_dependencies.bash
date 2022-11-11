#!/bin/bash
cd 
# install required spacy modules
python3 -m spacy download en_core_web_md

# unistall old version of docker if exists
apt remove docker docker-engine docker.io containerd runc

# update apt repository and packages list
apt update

# install dependencies
apt install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
chmod a+r /etc/apt/keyrings/docker.gpg
apt-get update

# install docker

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

