import subprocess
import os

def run(target):
    print("[+] Starting Fuzzing on common endpoints")
    output_dir = f"output/{target}/fuzzing/"
    os.makedirs(output_dir, exist_ok=True)
    # Placeholder for ffuf command
    with open(f"{output_dir}/result.txt", 'w') as f:
        f.write("FFUF fuzzing simulated output\n")
