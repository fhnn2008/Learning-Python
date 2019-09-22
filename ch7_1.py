fname = input("Enter file name: ")
fh = open(fname)
inp=fh.read()

for line in inp:
    line=line.strip()
    print(line.upper())
