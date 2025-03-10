#!/usr/bin/env python3
import requests
import json

# Read the prompt
with open("test_prompt.txt", "r") as f:
    prompt = f.read()

# Payload
payload = {
    "prompt": prompt,
    "max_tokens": 50,
    "temperature": 0.6
}

# Send request
response = requests.post("http://zeus:8080/v1/completions", json=payload)
print(response.text)

