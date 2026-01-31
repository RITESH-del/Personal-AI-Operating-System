import requests
import json

r = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "phi3:mini",
        "prompt": "hi"
    },
    stream=True
)

for line in r.iter_lines():
    if line:
        data = json.loads(line.decode("utf-8"))
        if "response" in data:
            print(data["response"], end="", flush=True)
