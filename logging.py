import requests

def scan(url):
    # Try to trigger an error
    test_url = url + "/nonexistent"
    try:
        res = requests.get(test_url, timeout=5)
        if res.status_code == 404:
            if "stack trace" in res.text.lower() or "error" in res.text.lower():
                return {"status": "Verbose Errors", "risk": "Medium"}
        return {"status": "Proper Error Handling", "risk": "Low"}
    except:
        return {"status": "Error", "risk": "Unknown"}