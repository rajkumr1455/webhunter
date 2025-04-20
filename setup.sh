#!/bin/bash

echo "[+] Installing dependencies..."

# Install Python dependencies
pip install -r requirements.txt

# Install additional system packages if necessary
sudo apt update
sudo apt install -y subfinder httpx nuclei ffuf

echo "[+] Installation complete."
