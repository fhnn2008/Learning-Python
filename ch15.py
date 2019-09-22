import re
import sqlite3

conn = sqlite3.connect('domain.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')


domains=list()
fh=open("mbox.txt")
for line in fh:
    if not line.startswith('From: '):continue
    line=line.rstrip()
    x=re.findall('@(\S*[^.])',line)
    for i in x:
        if len(x)>0:
            domains.append(i)


for d in range (len(domains)):
    org= domains[d]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
            VALUES (?, 1)''', (org,))
    else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                (org,))
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
