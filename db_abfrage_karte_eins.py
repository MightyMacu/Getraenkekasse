# -*- coding: utf-8 -*-

import sqlite3
import sys

try:
    shell = sys.stdout.shell
except AttributeError:
    raise RuntimeError("you must run this program in IDLE")

connection = sqlite3.connect("getraenkekasse.db")

cursor = connection.cursor()

connection.text_factory = str

def umlautEncode(s):
    encoded = ""
    for c in s:
        if c == ' ':
            encoded += " "
        elif c == '\xc3\xa3':
            encoded += "ā"
        elif c == ',':
            encoded += ", "
        elif c == '\xe2\x82\xac':
            encoded += "€"
        else:
            encoded += c
    return encoded 

shell.write("Dies ist deine Karten-ID:","BUILTIN")
print
shell.write("=========================","BUILTIN")
print

cursor.execute("SELECT * FROM kartenzuordnung WHERE uid='121,216,178,85'")
for c in cursor.fetchall():
    print (c[0]), umlautEncode(c[1]), (c[2])
    
shell.write("===================================","BUILTIN")
print
shell.write("Dies sind deine gekauften Getränke:","BUILTIN")
print
shell.write("===================================","BUILTIN")
print
print("DATUM & UHRZEIT (UTC) | GETRÄNKE NAME | GETRÄNKE PREIS")
print("======================================================")

cursor.execute("SELECT datum, getraenke_name, getraenke_preis FROM getraenke WHERE uid='121,216,178,85'")
for c in cursor.fetchall():
    print (c[0]), ("|"), (c[1]), ("|"), umlautEncode(c[2])

shell.write("===================================","BUILTIN")
print
shell.write("Dies ist die Summe deiner Ausgaben:","BUILTIN")
print
shell.write("===================================","BUILTIN")
print

cursor.execute("SELECT ROUND(SUM(getraenke_preis),2) FROM getraenke WHERE uid='121,216,178,85'")
result = cursor.fetchall()
for r in result:
    print(r), ('€')
    shell.write("------------------------------------------------------","BUILTIN")
    print

