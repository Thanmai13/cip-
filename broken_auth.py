import requests
from bs4 import BeautifulSoup

def scan(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        forms = soup.find_all('form')
        for form in forms:
            inputs = form.find_all('input')
            if any(inp.get('type') == 'password' for inp in inputs):
                # Found login form, check for weak indicators
                if not any(inp.get('name', '').lower() in ['csrf', 'token'] for inp in inputs):
                    return {"status": "Potentially Weak", "risk": "Medium", "reason": "No CSRF token"}
                return {"status": "Basic Auth Detected", "risk": "Low"}
        return {"status": "No Auth Forms", "risk": "Low"}
    except:
        return {"status": "Error", "risk": "Unknown"}