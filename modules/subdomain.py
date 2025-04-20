import subprocess
import os

def run(target):
    print("[+] Running Subdomain Enumeration")
    out_file = f"output/{target}/subdomains.txt"
    cmd = f"subfinder -d {target} -silent >> {out_file}"
    subprocess.run(cmd, shell=True)
    with open(out_file, 'r') as f:
        found = len(f.readlines())
    print(f"[+] Found {found} subdomains")
