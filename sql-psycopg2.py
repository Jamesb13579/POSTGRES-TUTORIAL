import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query one - select all records from the "artist" table
# cursor.execute('SELECT * FROM "Artist"')
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Green Day"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# result = cursor.fetchone()

# close the connection
connection.close()

#print results
for result in results:
    print (result)