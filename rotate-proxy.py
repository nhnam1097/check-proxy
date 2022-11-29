import requests
import csv
import concurrent.futures
import json

proxylist = []

# with open('proxylist.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         proxylist.append(row[0])


# r = requests.get('https://proxy6.net/api/4c89456dc9-d2bafc02d4-d532e6899f/getproxy')
# y = json.loads(r.text)
# print (y);

def extract(proxy):
    try:
        r= requests.get('https://httpbin.org/ip', proxies={'http': proxy}, timeout=3)
        print(r.json(), ' - working')
    except:
        # pass
        print(proxy, ' - not working')

extract('https://PRmhTm:MMPS5X@168.81.237.128:8000')

# with concurrent.futures.ThreadPoolExecutor() as exector:
#     exector.map(extract, proxylist)     