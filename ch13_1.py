import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# enter url
address = input('url: ')

#parse and read url
input = urllib.request.urlopen(address, context=ctx)
data = input.read()

#define a tree root from XML and iterate specific child
root = ET.fromstring(data)
lst=list()
for count in root.iter('count'):
    lst.append(int(count.text))

# print answers
print('Retrieved', len(data), 'characters')
print('Count',len(lst),'total= ', sum(lst))
