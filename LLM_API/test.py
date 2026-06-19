import requests

TOKEN = "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"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

r = requests.get(
    "https://huggingface.co/api/whoami-v2",
    headers=headers
)

print(r.status_code)
print(r.text)