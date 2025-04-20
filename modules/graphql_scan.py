import requests
import json

def run(target):
    print("[+] Running GraphQL Endpoint Detection")
    endpoints = ["/graphql", "/api/graphql", "/graphiql"]
    found = []

    for ep in endpoints:
        url = f"https://{target}{ep}"
        try:
            res = requests.post(url, json={"query": "{__typename}"}, timeout=5)
            if res.status_code == 200 and "data" in res.text:
                print(f"[+] Found GraphQL endpoint: {url}")
                found.append(url)
        except requests.RequestException:
            continue

    with open(f"output/{target}/graphql_findings.json", 'w') as f:
        json.dump({"endpoints": found}, f, indent=2)
