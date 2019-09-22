fh=open("mbox-short.txt")

d=dict()
l=list()
hourlist=list()
# Create a list of words.. email addresses
for line in fh:
    line=line.rstrip() # remove blank
    wds=line.split() # list of strings
    if len(wds)<1:continue # make sure there's no empty string
    if wds[0]!='From':continue # make sure contains email
    l.append(wds[5]) # append the word to the list
# Create a List
for t in l:
    hour =t.split(':')
    hourlist.append(hour[0])

# Code to create a histogram
for w in hourlist:
    d[w]=d.get(w,0)+1

# create a sorted list from a dictionary
x=sorted(d.items())

# print pairs
for k,v in x:
    print(k,v)
