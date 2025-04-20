#!/bin/bash

echo "[+] Setting up WebHunter..."

# Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Install subfinder (Go tool)
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

echo "[+] Setup complete!"
