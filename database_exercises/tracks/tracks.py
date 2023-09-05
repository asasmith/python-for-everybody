import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackDb.sqlite')
cursor = conn.cursor()

cursor.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fileHandle = open('Library.xml')

def lookup(data, key):
    found = False
    for item in data:
        if found : return item.text
        if item.tag == 'key' and item.text == key :
            found = True
    return None

rawData = ET.parse(fileHandle)
parsedData = rawData.findall('dict/dict/dict')

for item in parsedData:
    if (lookup(item, 'Track ID') is None):
        continue
    name = lookup(item, 'Name')
    artist = lookup(item, 'Artist')
    album = lookup(item, 'Album')
    genre = lookup(item, 'Genre')
    count = lookup(item, 'Play Count')
    rating = lookup(item, 'Rating')
    length = lookup(item, 'Total Time')

    if name is None or artist is None or album is None:
        continue
    if genre is None:
        genre = 'N/A'

    cursor.execute('insert or ignore into Artist (name) values (?)', (artist,))
    cursor.execute('select id from Artist where name = ?', (artist,))
    artist_id = cursor.fetchone()[0]

    cursor.execute('insert or ignore into Album (title, artist_id) values (?, ?)', (album, artist_id))
    cursor.execute('select id from Album where title = ?', (album,))
    album_id = cursor.fetchone()[0]

    cursor.execute('insert or ignore into Genre (name) values (?)', (genre,))
    cursor.execute('select id from Genre where name = ?', (genre,))
    genre_id = cursor.fetchone()[0]

    cursor.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ?)''', 
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()

cursor.execute(''' 
    SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
    AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
''')
rows = cursor.fetchall()

for item in rows:
    print(item[0], item[1], item[2], item[3])

