import argparse
from core.runner import run_module

def main():
    parser = argparse.ArgumentParser(description="WebHunter: Automated Pen Testing Tool")
    
    parser.add_argument("--subdomains", help="Enumerate subdomains", action="store_true")
    parser.add_argument("--graphql", help="Scan GraphQL endpoints", action="store_true")
    parser.add_argument("--httpx", help="Run httpx probe", action="store_true")
    parser.add_argument("--fuzz", help="Run fuzzing", action="store_true")
    parser.add_argument("--xss", help="Detect DOM-based XSS", action="store_true")
    parser.add_argument("--ssrf", help="Simulate SSRF vulnerability", action="store_true")

    args = parser.parse_args()

    if args.subdomains:
        run_module('subdomain')
    elif args.graphql:
        run_module('graphql_scan')
    elif args.httpx:
        run_module('httpx_probe')
    elif args.fuzz:
        run_module('fuzzing')
    elif args.xss:
        run_module('dom_xss')
    elif args.ssrf:
        run_module('ssrf_simulator')
    else:
        print("No valid module selected.")

if __name__ == "__main__":
    main()
