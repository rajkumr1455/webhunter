import requests

def send_alert(message, webhook_url):
    try:
        payload = {"text": message}
        response = requests.post(webhook_url, json=payload)
        if response.status_code != 200:
            print(f"[!] Failed to send alert: {response.text}")
    except Exception as e:
        print(f"[!] Error sending alert: {str(e)}")
