import requests

def scan(url):
    payload = "<script>alert(1)</script>"
    test_url = url + "?q=" + payload

    try:
        res = requests.get(test_url)
        if payload in res.text:
            return {"status": "Vulnerable", "risk": "High"}
        return {"status": "Safe", "risk": "Low"}
    except:
        return {"status": "Error", "risk": "Unknown"}