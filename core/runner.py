import os
from modules import (
    subdomain, graphql_scan, httpx_probe, web3_recon,
    nuclei_scan, fuzzing, dom_xss, ssrf_simulator
)

def run_modules(target, modules, profile):
    print(f"[+] Running WebHunter for: {target} | Profile: {profile}")
    os.makedirs(f"output/{target}", exist_ok=True)

    modules_to_run = modules.split(',') if modules != 'full' else [
        'subdomain', 'graphql', 'httpx', 'web3', 'nuclei', 'fuzzing', 'dom_xss', 'ssrf'
    ]

    if 'subdomain' in modules_to_run:
        subdomain.run(target)
    if 'graphql' in modules_to_run:
        graphql_scan.run(target)
    if 'httpx' in modules_to_run:
        httpx_probe.run(target)
    if 'web3' in modules_to_run:
        web3_recon.run(target)
    if 'nuclei' in modules_to_run:
        nuclei_scan.run(target)
    if 'fuzzing' in modules_to_run:
        fuzzing.run(target)
    if 'dom_xss' in modules_to_run:
        dom_xss.run(target)
    if 'ssrf' in modules_to_run:
        ssrf_simulator.run(target)
