from modules.subdomain import run_subdomain_enum
from modules.graphql_scan import run_graphql_scan
from modules.httpx_probe import run_httpx_probe
from modules.fuzzing import run_fuzzing
from modules.dom_xss import run_dom_xss
from modules.ssrf_simulator import run_ssrf_simulator

def run_module(module_name):
    if module_name == 'subdomain':
        run_subdomain_enum()
    elif module_name == 'graphql_scan':
        run_graphql_scan()
    elif module_name == 'httpx_probe':
        run_httpx_probe()
    elif module_name == 'fuzzing':
        run_fuzzing()
    elif module_name == 'dom_xss':
        run_dom_xss()
    elif module_name == 'ssrf_simulator':
        run_ssrf_simulator()
    else:
        print(f"Module {module_name} not found.")
