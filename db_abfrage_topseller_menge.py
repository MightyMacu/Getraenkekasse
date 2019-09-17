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

shell.write("Welches Getränk wird am meisten getrunken?","BUILTIN")
print
shell.write("==========================================","BUILTIN")
print
print("Getränkename | Menge")
print("====================")

cursor.execute("SELECT getraenke_name, count(*) anzahl FROM getraenke WHERE 1=1 GROUP BY getraenke_name ORDER BY count(*)  desc")
result = cursor.fetchall() 
for r in result:
    print str(r)

shell.write("-----------------------------------------","BUILTIN")
print

