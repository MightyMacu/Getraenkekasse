#!/usr/bin/python
#-*- coding: utf-8 -*-

import sqlite3
import RPi.GPIO as GPIO
import MFRC522
import signal
import logging
logging.basicConfig(filename='./FILENAME.log',
                    format='%(asctime)s - &(name) - %(levelname)s - %(message)s',
                    level = logging.DEBUG)

logger = logging.getLogger(__name__)

continue_reading = True

import sys

try:
    shell = sys.stdout.shell
except AttributeError:
    raise RuntimeError("you must run this program in IDLE")

#Verbindung zu Datenbank wird hergestellt 
connection = sqlite3.connect("getraenkekasse.db")

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# This loop keeps checking for chips. If one is near it will get the UID
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Card detected")
        break

# Get the UID of the card
(status,uid) = MIFAREReader.MFRC522_Anticoll()

# If we have the UID, continue
if status == MIFAREReader.MI_OK:

    #print UID
    _uid = str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3])
    print ("UID:", _uid)
    
#Create DB Cursor
cursor = connection.cursor()

#Check if UID is in DB
cursor.execute("SELECT * FROM kartenzuordnung WHERE uid = ?", (_uid,)) 

#Die Daten werden an die Datenbank übermittelt 
try:
    cursor.execute(""" INSERT INTO getraenke (getraenke_name, getraenke_preis, getraenke_menge, datum, uid)
VALUES  ("Mountain Dew", "1.05€", "1", DATETIME('now'), ?);""", (_uid,))

    connection.commit()
except (connection.Error, connection.Warning) as e:
    print(e)
finally:
    print ("1 Mountain Dew (0.50 l) wurde erfolgreich gebucht")
    print ("------------------------------------------------------")

connection.close()

#Verbindung zu Datenbank wird hergestellt 
connection = sqlite3.connect("getraenkekasse.db")

#Create DB Cursor
cursor = connection.cursor()

sql_command = """ UPDATE lager SET bestand = bestand - 1 WHERE getraenke_name = "Mountain Dew" """

cursor.execute(sql_command)

connection.commit()
            
print ("Die Datenbank wurde angepasst")
shell.write("-----------------------------", "BUILTIN")
print
                   
connection.close()
                   
