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

shell.write("Wer hat die meisten Getränke getrunken?","BUILTIN")
print
shell.write("=======================================","BUILTIN")
print
shell.write("Vorname | Nachname | Menge der Getränke","DEFINITION")
print
shell.write("=======================================","DEFINITION")
print

cursor.execute("SELECT kartenzuordnung.vorname, kartenzuordnung.nachname, count(*) anzahl FROM getraenke INNER JOIN kartenzuordnung ON (getraenke.uid = kartenzuordnung.uid) WHERE 1=1 GROUP BY getraenke.uid ORDER BY count(*)  desc")
for c in cursor.fetchall():
    print (c[0]), ("|"), (c[1]), ("|"), (c[2])

shell.write("------------------------------------------------------","BUILTIN")
print
