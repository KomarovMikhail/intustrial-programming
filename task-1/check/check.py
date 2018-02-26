import psycopg2

db = psycopg2.connect("dbname=postgres user=postgres password=postgres host=postgres port=5432")
cur = db.cursor()
cur.execute("""SELECT * FROM storage""")

rows = cur.fetchall()
for msg in rows:
    print(msg[0])

