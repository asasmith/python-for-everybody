import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS counts')
cursor.execute('CREATE TABLE counts (org TEXT, count INTEGER)')

fileHandle = open('mbox.txt')

for line in fileHandle:
    if line.startswith('From: '):
        line = line.strip()
        splitLine = line.split('@')
        org = splitLine[1]

        cursor.execute('SELECT count FROM counts WHERE org = ?', (org,))
        row = cursor.fetchone()

        if row is None:
            cursor.execute('INSERT INTO counts VALUES (?, 1)', (org,))
        else:
            cursor.execute('UPDATE counts SET count = count + 1 WHERE org = ?', (org,))

conn.commit()

query = 'SELECT org, count FROM counts ORDER BY count DESC LIMIT 1'

cursor.execute(query)
result = cursor.fetchone()

print(result[0], result[1])

cursor.close()
conn.close()
