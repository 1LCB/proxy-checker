import concurrent.futures
import requests

good_proxies = []

proxies_from_txt = open("proxies.txt", 'r')
proxies = list(map(lambda x: x.replace("\n", ""), proxies_from_txt))

def check_proxy(proxy: str):
    try:
        global good_proxies
        url = 'https://ipinfo.io/json'

        proxy_dict = {
            "http": proxy,
            "https": proxy,
        }
        response = requests.get(url, proxies=proxy_dict, timeout=2.5)
        print(f"{proxy} Works!")

        good_proxies.append(proxy)
    except:
        pass

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(check_proxy, proxies)

print(f"\n{len(good_proxies)} of {len(proxies)} proxies work")

with open(f"good_proxies.txt", "w+") as file:
    file.write("\n".join(good_proxies))





