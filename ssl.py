import requests

def scan(url):
    try:
        res = requests.get(url, timeout=5)
        if not url.startswith("https"):
            return {"status": "HTTP (Not Secure)", "risk": "High"}
        
        # Check cookies
        cookies = res.cookies
        insecure_cookies = []
        for cookie in cookies:
            if not cookie.secure:
                insecure_cookies.append(cookie.name)
        
        if insecure_cookies:
            return {"status": "Insecure Cookies", "risk": "Medium", "cookies": insecure_cookies}
        
        return {"status": "Secure", "risk": "Low"}
    except:
        return {"status": "Error", "risk": "Unknown"}