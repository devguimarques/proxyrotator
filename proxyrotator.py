import concurrent.futures
import requests
import csv

proxylist=[]

with open('proxylist.txt', 'r') as p:
    reader = csv.reader(p)
    for xproxy in reader:
        proxylist.append(xproxy[0])


def extract(proxy):
    try:
        r = requests.get('https://api.ipify.org?format=json', proxies={'http': proxy, 'https': proxy}, timeout=3)
        print('\033[1;32m', r.json(), '\033[m - proxy working')
    except:
        pass
    return proxy


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract, proxylist)