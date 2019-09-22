fh=open("mbox-short.txt")

d=dict()
l=list()
# Create a list of words.. email addresses
for line in fh:
    line=line.rstrip() # remove blank
    wds=line.split() # list of strings
    if len(wds)<1:continue # make sure there's no empty string
    if wds[0]!='From':continue # make sure contains email
    l.append(wds[1]) # append the word to the list
# Code to create a histogram
for w in l:
    d[w]=d.get(w,0)+1
# Code to calculate maximum
LargestKey=None
LargestValue=0
for k, v in d.items():
    if LargestValue<v:
        LargestValue=v
        LargestKey=k
print(LargestKey,LargestValue)
