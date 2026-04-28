import requests
import pickle
import base64

def scan(url):
    # Basic test for pickle deserialization (if Python app)
    payload = base64.b64encode(pickle.dumps({"test": "data"})).decode()
    try:
        res = requests.post(url, data={"data": payload}, timeout=5)
        if "test" in res.text:
            return {"status": "Potential Deserialization Issue", "risk": "High"}
        return {"status": "Safe", "risk": "Low"}
    except:
        return {"status": "Error", "risk": "Unknown"}