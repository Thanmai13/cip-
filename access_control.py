import requests

def scan(url):
    admin_paths = ["/admin", "/admin.php", "/wp-admin", "/administrator"]
    for path in admin_paths:
        test_url = url.rstrip('/') + path
        try:
            res = requests.get(test_url, timeout=5)
            if res.status_code == 200:
                return {"status": "Potential Access Control Issue", "risk": "Medium", "path": path}
        except:
            pass
    return {"status": "No Obvious Issues", "risk": "Low"}