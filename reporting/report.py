import json
import os

def generate_report(target, modules_output):
    report_path = f"output/{target}/report.html"
    with open(report_path, 'w') as report_file:
        report_file.write("<html><body>")
        report_file.write("<h1>WebHunter v1.4 - Bug Bounty Report</h1>")
        for module, findings in modules_output.items():
            report_file.write(f"<h2>{module}</h2>")
            report_file.write("<pre>" + json.dumps(findings, indent=2) + "</pre>")
        report_file.write("</body></html>")
    print(f"[+] Report generated at: {report_path}")
