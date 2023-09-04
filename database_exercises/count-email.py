import psycopg2

db_user = 'postgres'
db_password = 'themagicword'
db_name = 'py4e'
db_host = 'localhost'

try:
    conn = psycopg2.connect(
        dbname=db_name, user=db_user, password=db_password, host=db_host
    )
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Connected to PostgreSQL: {db_version}")

    cursor.execute('DROP TABLE IF EXISTS emails')
    cursor.execute('CREATE TABLE emails (email VARCHAR (50) UNIQUE NOT NULL, count INTEGER)')

    fileHandle = open('mbox-short.txt')

    for line in fileHandle:
        if line.startswith('From: '):
            splitLine = line.split(' ')
            email = splitLine[1]
            cursor.execute('SELECT count FROM emails WHERE email = %s', (email,))
            row = cursor.fetchone()

            if row is None:
                cursor.execute('INSERT INTO emails (email, count) VALUES (%s, 1)', (email,))
            else:
                cursor.execute('UPDATE emails SET count = count + 1 WHERE email = %s', (email,))

            conn.commit()

    query = 'SELECT email, count FROM emails ORDER BY count DESC LIMIT 10'

    cursor.execute(query)
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(str(row[0]), str(row[1]))
    else:
        print('No results found')

    cursor.close()
    conn.close()
except Exception as e:
    print('in the exception')
    print(f"Error connecting to PostgreSQL: {e}")

