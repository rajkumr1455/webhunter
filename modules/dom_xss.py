import requests
from bs4 import BeautifulSoup

def run_dom_xss():
    url = "http://example.com"
    print(f"Scanning {url} for DOM-based XSS...")
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if "document.location" in str(soup):
        print("Potential DOM-based XSS vulnerability detected!")
    else:
        print("No DOM-based XSS found.")
