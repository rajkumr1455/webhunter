#!/bin/bash

echo "[+] Installing necessary tools..."

# Install Go
sudo apt install -y golang-go

# Install httpx
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

echo "[+] Tools installation complete!"
