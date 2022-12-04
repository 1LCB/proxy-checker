from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0"
}

site = requests.get('https://free-proxy-list.net', headers=headers).content

soup = BeautifulSoup(site, "html.parser")
tabela = soup.find("table", {"class": "table table-striped table-bordered"})

tds = tabela.find_all("td")

proxies = []

for i in range(0, len(tds), 8):
    anonymity = tds[i + 4].text
    if anonymity != "elite proxy":
        continue

    ip = tds[i].text
    port = tds[i + 1].text
    proxies.append(f'{ip}:{port}')

with open("proxies.txt", "w+") as file:
    file.write("\n".join(proxies))

print("your proxies were saved in proxies.txt!")