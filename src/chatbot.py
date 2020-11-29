import requests

def ask(msg) -> str:
    resp = requests.get(
        "https://some-random-api.ml/chatbot",
        {
            "message": msg
        }
    )

    data = resp.json()

    try:
        return data["response"]

    except KeyError:
        return "Try Again."