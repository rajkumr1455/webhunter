import os

def run(target):
    print("[+] Simulating SSRF callbacks")
    with open(f"output/{target}/ssrf_sim.log", 'w') as f:
        f.write("SSRF simulation initiated - use Burp Collaborator or interactsh\n")
