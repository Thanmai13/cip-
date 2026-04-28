import requests
from bs4 import BeautifulSoup

def scan(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        scripts = soup.find_all('script', src=True)
        vulnerable_libs = []
        
        known_vulns = {
            "jquery-1.": "Old jQuery version",
            "bootstrap-2.": "Old Bootstrap",
            "angular-1.": "Old Angular"
        }
        
        for script in scripts:
            src = script['src']
            for vuln in known_vulns:
                if vuln in src:
                    vulnerable_libs.append(known_vulns[vuln])
        
        if vulnerable_libs:
            return {"status": "Vulnerable Components", "risk": "Medium", "libs": vulnerable_libs}
        return {"status": "No Known Issues", "risk": "Low"}
    except:
        return {"status": "Error", "risk": "Unknown"}