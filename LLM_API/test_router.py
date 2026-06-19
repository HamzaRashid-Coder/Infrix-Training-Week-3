import requests

TOKEN = "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"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "model": "Qwen/Qwen2.5-7B-Instruct",
    "messages": [
        {
            "role": "user",
            "content": "Hello"
        }
    ]
}

r = requests.post(
    "https://router.huggingface.co/v1/chat/completions",
    headers=headers,
    json=payload
)

print(r.status_code)
print(r.text)