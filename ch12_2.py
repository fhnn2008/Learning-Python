import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Enter the first url, count and position
url = input('Enter - ')
count=int(input("Enter count= "))
position = int(input("Enter position= "))
# loop through the program by number entered in "count"
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()# open and read html
    soup = BeautifulSoup(html, 'html.parser')# beautifull soup decode and parse

# Retrieve all of the anchor tags
    addresses=list()
    tags = soup('a')
    for tag in tags:
        address = str(tag.get('href', None))
        addresses.append(address) # byilds a list of strings

    url=addresses[position-1]# picks the new url based on the position in the list
    print(url)
