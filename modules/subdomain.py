import subprocess

def run_subdomain_enum():
    domain = "example.com"
    print(f"Starting subdomain enumeration for {domain}...")
    result = subprocess.run(['subfinder', '-d', domain], capture_output=True, text=True)
    print("Subdomains found:")
    print(result.stdout)
