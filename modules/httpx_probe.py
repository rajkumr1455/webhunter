import subprocess
import os

def run(target):
    print("[+] Probing for live hosts with httpx")
    input_file = f"output/{target}/subdomains.txt"
    output_file = f"output/{target}/httpx.json"
    cmd = f"cat {input_file} | httpx -json -title -status-code -tech-detect -silent > {output_file}"
    subprocess.run(cmd, shell=True)
