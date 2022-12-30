from threading import Thread
import time
import requests

MAX_THREADS = 5
WORKING_THREADS = 0

good_proxies = []

with open('proxies.txt', 'r') as file:
    proxies = file.read().split('\n')


def check_proxy(proxy: str):
    global good_proxies, WORKING_THREADS
    try:
        WORKING_THREADS += 1
        url = 'https://ipinfo.io/json'  # https://ipinfo.io/json https://www.myip.com

        proxy_dict = {
            "http": proxy,
            "https": proxy,
        }
        print(f"checking {proxy}...")
        response = requests.get(url, proxies=proxy_dict, timeout=15)
        print(f"{proxy} Works!\n")
        # print(response.text)

        good_proxies.append(proxy)

        WORKING_THREADS -= 1
    except:
        WORKING_THREADS -= 1


for proxy in proxies:
    while WORKING_THREADS == MAX_THREADS:
        time.sleep(0.5)
    t = Thread(target=check_proxy, args=(proxy,))
    t.start()

print(f"\n{len(good_proxies)} of {len(proxies)} proxies work")

with open(f"good_proxies.txt", "w+") as file:
    file.write("\n".join(good_proxies))

input("Press enter to exit")