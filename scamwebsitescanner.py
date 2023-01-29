import requests
from bs4 import BeautifulSoup

def check_scam(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("title").text
        if "404" in title or "error" in title:
            return True
        else:
            return False
    except:
        return True

url = "https://www.example.com"
if check_scam(url):
    print(f"{url} is a scam.")
else:
    print(f"{url} is not a scam.")
