import os

def generate_report(target, modules):
    print("[+] Generating Report for", target)
    report_file = f"output/{target}/webhunter_report.md"
    with open(report_file, 'w') as f:
        f.write(f"# WebHunter Report for {target}\n")
        f.write(f"Modules run: {', '.join(modules)}\n")
        f.write("\n## Findings:\n")
        # Placeholder for actual findings and results
        f.write("No findings yet...\n")
    print(f"[+] Report generated at {report_file}")
