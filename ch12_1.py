from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


# Retrieve "span" of the anchor tags and extract numbers and sum all of them
numbers=list()
tags=soup('span')
for tag in tags:
    line=str(tag)
    x=re.findall('[0-9]+',line) # find the numbers
    if len(x)>0:
        for i in x:
            numbers.append(float(i))# feed the list

print("sum=",int(sum(numbers)))# add and print
