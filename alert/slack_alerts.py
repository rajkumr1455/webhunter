import requests

def send_slack_alert(message):
    slack_webhook_url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
    payload = {"text": message}
    response = requests.post(slack_webhook_url, json=payload)
    
    if response.status_code == 200:
        print("Alert sent to Slack.")
    else:
        print(f"Failed to send alert. Status code: {response.status_code}")
