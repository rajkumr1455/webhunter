import subprocess
import os

def run(target):
    print("[+] Running Nuclei scan")
    input_file = f"output/{target}/httpx.json"
    output_file = f"output/{target}/nuclei_findings.yaml"
    cmd = f"cat {input_file} | jq -r '.[].input' | nuclei -silent -json -o {output_file}"
    subprocess.run(cmd, shell=True)
