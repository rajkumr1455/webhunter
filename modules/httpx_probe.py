import subprocess

def run_httpx_probe():
    domain = "example.com"
    print(f"Starting HTTP probe for {domain}...")
    result = subprocess.run(['httpx', '-u', domain, '-title', '-status-code'], capture_output=True, text=True)
    print("HTTP probe results:")
    print(result.stdout)
