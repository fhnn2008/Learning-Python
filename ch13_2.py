import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# enter url
address = input("url: ")


#open,handle and read url
input = urllib.request.urlopen(address, context=ctx)
data = input.read()

#transform from json to python element
js = json.loads(data.decode())

# find the correct address in json
list=js["comments"]

#loop through and add up all 'counts'
total=0
for item in list:
    x=int(item['count'])
    total=total +x

print(total)
