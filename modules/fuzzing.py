import requests

def run_fuzzing():
    target = "http://example.com"
    paths = ["admin", "login", "dashboard"]
    
    print(f"Starting fuzzing on {target}...")
    
    for path in paths:
        url = f"{target}/{path}"
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"Found valid path: {url}")
        else:
            print(f"Invalid path: {url}")
