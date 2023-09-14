#!/usr/bin/bash

echo "Set vars"
export OS="xUbuntu_22.04"
export VERSION="1.24"


echo "Grab keyrings."
echo "Archive..."
echo "deb [signed-by=/usr/share/keyrings/libcontainers-archive-keyring.gpg] https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/ /" > /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list

echo "crio-archive..."
echo "deb [signed-by=/usr/share/keyrings/libcontainers-crio-archive-keyring.gpg] https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/$VERSION/$OS/ /" > /etc/apt/sources.list.d/devel:kubic:libcontainers:stable:cri-o:$VERSION.list

echo "Store de-armored keyrings in /usr/share/keyrings."
mkdir -p /usr/share/keyrings

echo "Standard..."
curl -s -L https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS/Release.key | gpg --dearmor -o /usr/share/keyrings/libcontainers-archive-keyring.gpg

echo "cri-o..."
curl -s -L https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/$VERSION/$OS/Release.key | gpg --dearmor -o /usr/share/keyrings/libcontainers-crio-archive-keyring.gpg

echo "Update and install."
apt-get -qq update
apt-get -qq install -y cri-o cri-o-runc 

echo "Reload and enable."
systemctl daemon-reload
systemctl enable crio
systemctl start crio

echo "Done."

## Notes: 
# Followed the cri-o installation guide at: 
# https://github.com/cri-o/cri-o


