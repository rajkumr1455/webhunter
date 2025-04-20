import json

def generate_report(results):
    report_file = "scan_report.json"
    with open(report_file, 'w') as f:
        json.dump(results, f, indent=4)
    print(f"Report saved to {report_file}")
