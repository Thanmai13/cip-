import requests

def scan(url):
    try:
        res = requests.get(url, timeout=5)
        headers = res.headers

        missing = []
        issues = []

        required_headers = ["Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options", "Strict-Transport-Security"]
        for header in required_headers:
            if header not in headers:
                missing.append(header)

        if "Server" in headers and "Apache" in headers["Server"]:
            issues.append("Server version exposed")

        if missing or issues:
            return {"status": "Misconfigured", "missing": missing, "issues": issues, "risk": "Medium"}
        return {"status": "Secure", "risk": "Low"}
    except:
        return {"status": "Error", "risk": "Unknown"}