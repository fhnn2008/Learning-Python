import re
fh=open("Actual.txt")
numbers=list()
count=0
for line in fh:
    line=line.rstrip()
    x=re.findall('[0-9]+',line)
    if len(x)>0:
        for i in x:
            numbers.append(float(i))
            count=count+1
print("sum=",int(sum(numbers)))
