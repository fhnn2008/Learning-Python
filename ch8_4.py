fname = input("Enter file name: ")
fh = open(fname)
lst=list()
for line in fh:
    line.rstrip()
    x=line.split()
    for i in range(len(x)):
        if x[i] in lst:continue
        lst.append(x[i])
        lst.sort()
print(lst)
