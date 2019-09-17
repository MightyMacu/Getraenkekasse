import sqlite3
connection = sqlite3.connect("getraenkekasse.db")

cursor = connection.cursor()

sql_command = """
CREATE TABLE getraenke ( 
buchung_nummer INTEGER PRIMARY KEY, 
getraenke_name VARCHAR(20), 
getraenke_preis NUMERIC,
getraenke_menge INT NOT NULL, 
uid NUMBER,
datum DATETIME
);"""

cursor.execute(sql_command)

sql_command = """
CREATE TABLE kartenzuordnung ( 
uid NUMBER NOT NULL PRIMARY KEY, 
vorname VARCHAR(20), 
nachname VARCHAR(20) 
);"""

cursor.execute(sql_command)

sql_command = """
CREATE TABLE lager ( 
bestand NUMBER,  
getraenke_name VARCHAR(20) PRIMARY KEY
);"""

cursor.execute(sql_command)

connection.commit()

connection.close()
