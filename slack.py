import requests
import argparse

def send_slack_message(str):
    payload = '{"text": "%s"}' % str
    response = requests.post('https://hooks.slack.com/services/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', data = payload)
    print(response.text)