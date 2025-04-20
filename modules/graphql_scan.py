import requests

def run_graphql_scan():
    url = "https://example.com/graphql"
    headers = {"Content-Type": "application/json"}
    query = "{ __schema { types { name } } }"
    response = requests.post(url, json={'query': query}, headers=headers)
    
    if response.status_code == 200:
        print("GraphQL endpoint is reachable.")
        print("Response:", response.json())
    else:
        print(f"Failed to reach GraphQL endpoint. Status code: {response.status_code}")
