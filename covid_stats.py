import requests
from bs4 import BeautifulSoup

url = f"https://www.worldometers.info/coronavirus/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

cases, deaths, recovered = soup.select(".maincounter-number")

print(f"Cases: {cases.text.strip()}")
print(f"Deaths: {deaths.text.strip()}")
print(f"Recovered: {recovered.text.strip()}")