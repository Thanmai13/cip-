import requests

def scan(url):
    payloads = ["; ls", "| ls", "`ls`", "$(ls)"]
    for payload in payloads:
        test_url = url + "?cmd=" + payload
        try:
            res = requests.get(test_url, timeout=5)
            if "bin" in res.text or "etc" in res.text or "passwd" in res.text:
                return {"status": "Vulnerable", "risk": "High", "payload": payload}
        except:
            pass
    return {"status": "Safe", "risk": "Low"}