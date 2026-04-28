import requests

def scan(url):
    test_url = url + "?id=1' OR '1'='1"
    try:
        res = requests.get(test_url)
        if "error" in res.text.lower() or "sql" in res.text.lower():
            return {"status": "Vulnerable", "risk": "High"}
        return {"status": "Safe", "risk": "Low"}
    except:
        return {"status": "Error", "risk": "Unknown"}