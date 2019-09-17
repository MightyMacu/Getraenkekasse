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

shell.write("Welche Getränke sind noch da?","BUILTIN")
print
shell.write("=============================","BUILTIN")
print
shell.write("Menge | Getränkename","DEFINITION")
print
shell.write("====================","DEFINITION")
print

cursor.execute("SELECT * FROM lager ORDER BY getraenke_name")
result = cursor.fetchall() 
for r in result:
    print(r)

shell.write("----------------------------", "BUILTIN")
print

