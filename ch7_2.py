# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
tot=0
count=0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line=line.rstrip()
    pos=line.find(".")
    slice= line[pos-1:pos+5]
    num=float(slice)
    tot=tot+num
    count=count+1

print("Average spam confidence:",float(tot/count))
