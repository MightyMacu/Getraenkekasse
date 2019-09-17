import sqlite3
connection = sqlite3.connect("getraenkekasse.db")

cursor = connection.cursor()

#sql_command = """ INSERT INTO getraenke (getraenke_name, getraenke_preis, getraenke_menge, rfid_id)
#    VALUES  ("Astra_groß", "0,40€", 1, "rfid_id");"""
sql_command = """ INSERT INTO kartenzuordnung (uid, vorname, nachname)
    VALUES ("105,14,37,99", "Michael", "Bernegger");"""
#sql_command = """ DELETE FROM getraenke WHERE buchung_nummer = (SELECT MAX(buchung_nummer) FROM getraenke)"""
#sql_command = """ DELETE FROM getraenke WHERE buchung_nummer = 3"""
#sql_command = """ INSERT INTO lager (bestand, getraenke_name)
#    VALUES ("1", "IRN BRU");"""
#sql_command = """ UPDATE getraenke SET uid = "89,144,165,99" WHERE buchung_nummer = 20 """

cursor.execute(sql_command)

connection.commit()

connection.close()
