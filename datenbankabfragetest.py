import sqlite3
connection = sqlite3.connect("getraenkekasse.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM getraenke INNER JOIN kartenzuordnung ON getraenke.uid = kartenzuordnung.uid")
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)
cursor.execute("SELECT * FROM getraenke INNER JOIN kartenzuordnung ON getraenke.uid = kartenzuordnung.uid") 
print("\nfetch one:")
res = cursor.fetchone() 
print(res)

cursor.execute("SELECT * FROM kartenzuordnung")
print("\nfetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)

cursor.execute("SELECT * FROM lager")
print("\nfetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)
