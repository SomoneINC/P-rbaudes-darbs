import requests
import time
import re
from bs4 import BeautifulSoup

url = "http://r64vsk.lv/"
request = requests.get(url)
time.sleep(1)
soup = BeautifulSoup(request.text, "html.parser")
Saraksts = soup.find('div', class_="r64-events").text
printed = False
lines_list = Saraksts.splitlines()
while True:
    print("Kura klases izmaiņas gribat zināt? \n")
    user=input()
    for line in lines_list:
        if user.lower() in line.lower():
            printed = True
            print(line)
    if printed == False:
        print("Nekas nav atrasts") 
    printed = False
