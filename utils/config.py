import os

def get_config():
    config = {
        "slack_webhook_url": os.getenv("SLACK_WEBHOOK_URL", ""),
        "report_format": "markdown"
    }
    return config
