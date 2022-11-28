import requests
import csv
import concurrent.futures

proxylist = []

with open('proxylist.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])

def extract(proxy):
    try:
        r= requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https': proxy}, timeout=3)
        print(r.json(), ' - working')
    except:
        # pass
        print(proxy, ' - not working')

# extract('168.81.237.128:8000:PRmhTm:MMPS5X')

with concurrent.futures.ThreadPoolExecutor() as exector:
    exector.map(extract, proxylist)     