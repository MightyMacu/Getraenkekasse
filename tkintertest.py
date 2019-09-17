import Tkinter #in python 3.x: tkinter wird kleingeschrieben
import sys
import os
from Tkinter import *
from ttk import *

#################################
#Scripte für Getränke:          #
#################################
#Script für ein großes Astra Urtyp
def Astra_urtyp_gross():
    exec(compile(open('buchung_astra_urtyp_groß.py', "rb").read(), 'buchung_astra_urtyp_groß.py', 'exec'))
#Script für ein kleines Astra Urtyp
def Astra_urtyp_klein():
    exec(compile(open('buchung_astra_urtyp_klein.py', "rb").read(), 'buchung_astra_urtyp_klein.py', 'exec'))
#Script für ein kleines Astra Rotlicht
def Astra_rotlicht_klein():
    exec(compile(open('buchung_astra_rotlicht_klein.py', "rb").read(), 'buchung_astra_rotlicht_klein.py', 'exec'))
#Script für ein kleines Astra Kiezmische
def Astra_kiezmische_klein():
    exec(compile(open('buchung_astra_kiezmische_klein.py', "rb").read(), 'buchung_astra_kiezmische_klein.py', 'exec'))
#Script für ein kleines Astra Rakete
def Astra_rakete_klein():
    exec(compile(open('buchung_astra_rakete_klein.py', "rb").read(), 'buchung_astra_rakete_klein.py', 'exec'))
#Script für ein bullit klein
def bullit_klein():
    exec(compile(open('buchung_bullit_klein.py', "rb").read(), 'buchung_bullit_klein.py', 'exec'))
#Script für eine große Fritz-limo
def Fritz_Limo_gross():
    exec(compile(open('buchung_fritz_limo_groß.py', "rb").read(), 'buchung_fritz_limo_groß.py', 'exec'))
#Script für eine kleine Fritz-limo
def Fritz_Limo_klein():
    exec(compile(open('buchung_fritz_limo_klein.py', "rb").read(), 'buchung_fritz_limo_klein.py', 'exec'))
#Script für ein Mountain Dew
def Mountain_Dew():
    exec(compile(open('buchung_Mountain_Dew.py', "rb").read(), 'buchung_Mountain_Dew.py', 'exec'))
#Script für ein Monster 0.5l
def Monster():
    exec(compile(open('buchung_monster_groß.py', "rb").read(), 'buchung_monster_groß.py', 'exec'))
#Script für ein kleines Ratsherrn Pilsener
def Ratsherrn_pilsener_klein():
    exec(compile(open('buchung_ratsherrn_pilsener_klein.py', "rb").read(), 'buchung_ratsherrn_pilsener_klein.py', 'exec'))
#Script für ein kleines Red Bull
def red_bull_klein():
    exec(compile(open('buchung_red_bull_klein.py', "rb").read(), 'buchung_red_bull_klein.py', 'exec'))
#Script für ein großes Red Bull
def red_bull_gross():
    exec(compile(open('buchung_red_bull_groß.py', "rb").read(), 'buchung_red_bull_groß.py', 'exec'))
#Script für ein Rothaus Pils Tannenzäpfle
def rothaus_tannenzaepfle():
    exec(compile(open('buchung_rothaus_tannenzäpfle.py', "rb").read(), 'buchung_rothaus_tannenzäpfle.py', 'exec'))
#Script für ein kleines Astra
def Astra_klein():
    exec(compile(open('buchung_astra_klein.py', "rb").read(), 'buchung_astra_klein.py', 'exec'))
#Script für eine Bionade
def bionade():
    exec(compile(open('buchung_bionade.py', "rb").read(), 'buchung_bionade.py', 'exec'))
#Script für einen 28 Black
def schwarzedose():
    exec(compile(open('buchung_28_black.py', "rb").read(), 'buchung_28_black.py', 'exec'))
#Script für ein Krombacher Radler
def krombacher_radler():
    exec(compile(open('buchung_krombacher_radler.py', "rb").read(), 'buchung_krombacher_radler.py', 'exec'))
#Script für ein Ratsherrn New Era
def Ratsherrn_new_era():
    exec(compile(open('buchung_ratsherrn_new_era.py', "rb").read(), 'buchung_ratsherrn_new_era.py', 'exec'))
#Script für eine Fritz-kola grün und gerecht
def fritz_gruen():
    exec(compile(open('buchung_fritz_gruen.py', "rb").read(), 'buchung_fritz_gruen.py', 'exec'))
#Script für ein IRN BRU
def IRN_BRU():
    exec(compile(open('buchung_irn_bru.py', "rb").read(), 'buchung_irn_bru.py', 'exec'))

################################################
#Scripte für die Abfrage von Buchungen:        #
################################################
#Script für die Buchungen von Person Eins
def db_abfrage_person_eins():
    exec(compile(open('db_abfrage_person_eins.py', "rb").read(), 'db_abfrage_person_eins.py', 'exec'))
#Script für die Buchungen von Person Zwei 
def db_abfrage_person_zwei():
    exec(compile(open('db_abfrage_person_zwei.py', "rb").read(), 'db_abfrage_person_zwei.py', 'exec'))
#Script für die Buchungen von Person Drei
def db_abfrage_person_drei():
    exec(compile(open('db_abfrage_person_drei.py', "rb").read(), 'db_abfrage_person_drei.py', 'exec'))
#Script für die Buchungen von Person Vier 
def db_abfrage_person_vier():
    exec(compile(open('db_abfrage_person_vier.py', "rb").read(), 'db_abfrage_person_vier.py', 'exec'))
#Script für die Buchungen von Person Fünf
def db_abfrage_person_fuenf():
    exec(compile(open('db_abfrage_person_fünf.py', "rb").read(), 'db_abfrage_person_fünf.py', 'exec'))
#Script für die Buchungen von Person Sechs
def db_abfrage_person_sechs():
    exec(compile(open('db_abfrage_person_sechs.py', "rb").read(), 'db_abfrage_person_sechs.py', 'exec'))
#Script für die Buchungen von Person Sieben 
def db_abfrage_person_sieben():
    exec(compile(open('db_abfrage_person_sieben.py', "rb").read(), 'db_abfrage_person_sieben.py', 'exec'))
#Script für die Buchungen von Person Acht
def db_abfrage_person_acht():
    exec(compile(open('db_abfrage_person_acht.py', "rb").read(), 'db_abfrage_person_acht.py', 'exec'))
#Script für die Buchungen von Person Neun
def db_abfrage_person_neun():
    exec(compile(open('db_abfrage_person_neun.py', "rb").read(), 'db_abfrage_person_neun.py', 'exec'))
#Script für die Buchungen von Person Zehn
def db_abfrage_person_zehn():
    exec(compile(open('db_abfrage_person_zehn.py', "rb").read(), 'db_abfrage_person_zehn.py', 'exec'))
#Script für die Buchungen von Person Elf
def db_abfrage_person_elf():
    exec(compile(open('db_abfrage_person_elf.py', "rb").read(), 'db_abfrage_person_elf.py', 'exec'))
#Script für die Buchungen von Person Zwölf
def db_abfrage_person_zwoelf():
    exec(compile(open('db_abfrage_person_zwoelf.py', "rb").read(), 'db_abfrage_person_zwoelf.py', 'exec'))
#Script für die Buchungen von Person Dreizehn
def db_abfrage_person_dreizehn():
    exec(compile(open('db_abfrage_person_dreizehn.py', "rb").read(), 'db_abfrage_person_dreizehn.py', 'exec'))
#Script für die Buchungen von Karte Eins
def db_abfrage_karte_eins():
    exec(compile(open('db_abfrage_karte_eins.py', "rb").read(), 'db_abfrage_karte_eins.py', 'exec'))
#Script für die Buchungen von Karte Zwei
def db_abfrage_karte_zwei():
    exec(compile(open('db_abfrage_karte_zwei.py', "rb").read(), 'db_abfrage_karte_zwei.py', 'exec'))
#Script für die Buchungen von Karte Drei
def db_abfrage_karte_drei():
    exec(compile(open('db_abfrage_karte_drei.py', "rb").read(), 'db_abfrage_karte_drei.py', 'exec'))
#Script für die Buchungen von Karte Vier
def db_abfrage_karte_vier():
    exec(compile(open('db_abfrage_karte_vier.py', "rb").read(), 'db_abfrage_karte_vier.py', 'exec'))
#Script für die Buchungen von Karte Fünf
def db_abfrage_karte_fuenf():
    exec(compile(open('db_abfrage_karte_fünf.py', "rb").read(), 'db_abfrage_karte_fünf.py', 'exec'))

#########################################
#Abfrage der monatlichen Buchungen:     #
#########################################
#Person Eins
def db_abfrage_person_eins_monat():
    exec(compile(open('db_abfrage_person_eins_monat.py', "rb").read(), 'db_abfrage_person_eins_monat.py', 'exec'))
#Person Zwei
def db_abfrage_person_zwei_monat():
    exec(compile(open('db_abfrage_person_zwei_monat.py', "rb").read(), 'db_abfrage_person_zwei_monat.py', 'exec'))
#Person Drei
def db_abfrage_person_drei_monat():
    exec(compile(open('db_abfrage_person_drei_monat.py', "rb").read(), 'db_abfrage_person_drei_monat.py', 'exec'))
#Person Vier 
def db_abfrage_person_vier_monat():
    exec(compile(open('db_abfrage_person_vier_monat.py', "rb").read(), 'db_abfrage_person_vier_monat.py', 'exec'))
#Person Fünf
def db_abfrage_person_fuenf_monat():
    exec(compile(open('db_abfrage_person_fünf_monat.py', "rb").read(), 'db_abfrage_person_fünf_monat.py', 'exec'))
#Person Sechs
def db_abfrage_person_sechs_monat():
    exec(compile(open('db_abfrage_person_sechs_monat.py', "rb").read(), 'db_abfrage_person_sechs_monat.py', 'exec'))
#Person Sieben 
def db_abfrage_person_sieben_monat():
    exec(compile(open('db_abfrage_person_sieben_monat.py', "rb").read(), 'db_abfrage_person_sieben_monat.py', 'exec'))
#Person Acht
def db_abfrage_person_acht_monat():
    exec(compile(open('db_abfrage_person_acht_monat.py', "rb").read(), 'db_abfrage_person_acht_monat.py', 'exec'))
#Person Neun
def db_abfrage_person_neun_monat():
    exec(compile(open('db_abfrage_person_neun_monat.py', "rb").read(), 'db_abfrage_person_neun_monat.py', 'exec'))
#Person Zehn
def db_abfrage_person_zehn_monat():
    exec(compile(open('db_abfrage_person_zehn_monat.py', "rb").read(), 'db_abfrage_person_zehn_monat.py', 'exec'))
#Person Elf
def db_abfrage_person_elf_monat():
    exec(compile(open('db_abfrage_person_elf_monat.py', "rb").read(), 'db_abfrage_person_elf_monat.py', 'exec'))
#Person Zwölf
def db_abfrage_person_zwoelf_monat():
    exec(compile(open('db_abfrage_person_zwoelf_monat.py', "rb").read(), 'db_abfrage_person_zwoelf_monat.py', 'exec'))
#Person Dreizehn
def db_abfrage_person_dreizehn_monat():
    exec(compile(open('db_abfrage_person_dreizehn_monat.py', "rb").read(), 'db_abfrage_person_dreizehn_monat.py', 'exec'))
#Karte Eins
def db_abfrage_karte_eins_monat():
    exec(compile(open('db_abfrage_karte_eins_monat.py', "rb").read(), 'db_abfrage_karte_eins_monat.py', 'exec'))
#Karte Zwei
def db_abfrage_karte_zwei_monat():
    exec(compile(open('db_abfrage_karte_zwei_monat.py', "rb").read(), 'db_abfrage_karte_zwei_monat.py', 'exec'))
#Karte Drei
def db_abfrage_karte_drei_monat():
    exec(compile(open('db_abfrage_karte_drei_monat.py', "rb").read(), 'db_abfrage_karte_drei_monat.py', 'exec'))
#Karte Vier
def db_abfrage_karte_vier_monat():
    exec(compile(open('db_abfrage_karte_vier_monat.py', "rb").read(), 'db_abfrage_karte_vier_monat.py', 'exec'))
#Karte Fünf
def db_abfrage_karte_fuenf_monat():
    exec(compile(open('db_abfrage_karte_fünf_monat.py', "rb").read(), 'db_abfrage_karte_fünf_monat.py', 'exec'))

##############################################
#Scripte für Extras:                         #
##############################################
#Wer hat am meisten Getränke gebucht?
def db_abfrage_getraenke_menge():
    exec(compile(open('db_abfrage_getraenke_menge.py', "rb").read(), 'db_abfrage_getraenke_menge.py', 'exec'))
#Welche Getränke werden am meisten gebucht:
def db_abfrage_topseller_menge():
    exec(compile(open('db_abfrage_topseller_menge.py', "rb").read(), 'db_abfrage_topseller_menge.py', 'exec'))
#Welche Getränke sind noch da:
def db_abfrage_bestand():
    exec(compile(open('db_abfrage_bestand.py', "rb").read(), 'db_abfrage_bestand.py', 'exec'))
    
#####################################
#Tkinter Umgebung:                  #
#####################################
mainWin = Tkinter.Tk()
mainWin.title('Getränkekasse')
mainFrame = Tkinter.Frame(mainWin, borderwidth=10, relief='ridge')
mainFrame.grid()

######################################
#Erste Spalte, Getränk wählen:       #
######################################
label_1 = Tkinter.Label(text="Bitte wähle ein Getränk aus!", borderwidth=2, relief="groove")
label_1.grid(column=1, row=1)
######################################
#Buttons für jedes Getränk:          #
######################################
button_2 = Tkinter.Button(text="28 Black (0.25 l)",command=schwarzedose, height=1, width=30, activebackground="green")
button_2.grid(column=1, row=3)
button_2 = Tkinter.Button(text="Astra klein \n Kiezmische / Rakete / \n Rotlicht / Urtyp (0.33 l)",command=Astra_klein, height=3, width=30, activebackground="green")
button_2.grid(column=1, row=4)
#button_2 = Tkinter.Button(text="Astra Rakete klein (0.33 l)",command=Astra_rakete_klein, height=1, width=30, activebackground="green")
#button_2.grid(column=1, row=4)
#button_2 = Tkinter.Button(text="Astra Rotlicht klein (0.33 l)",command=Astra_rotlicht_klein, height=1, width=30, activebackground="green")
#button_2.grid(column=1, row=5)
button_1 = Tkinter.Button(text="Astra Urtyp groß (0.50 l)",command=Astra_urtyp_gross, height=1, width=30, activebackground="green")
button_1.grid(column=1, row=5)
#button_2 = Tkinter.Button(text="Astra Urtyp klein (0.33 l)",command=Astra_urtyp_klein, height=1, width=30, activebackground="green")
#button_2.grid(column=1, row=7)
button_2 = Tkinter.Button(text="Bionade (0.33 l)",command=bionade, height=1, width=30, activebackground="green")
button_2.grid(column=1, row=6)
button_2 = Tkinter.Button(text="BULLIT klein (0.50 l)",command=bullit_klein, height=1, width=30, activebackground="green")
button_2.grid(column=1, row=7)
button_3 = Tkinter.Button(text="Fritz-kola grün und gerecht (0.33 l)",command=fritz_gruen, height=1, width=30, activebackground="green")
button_3.grid(column=1, row=8)
button_3 = Tkinter.Button(text="Fritz-limo / Fritz-kola groß (0.50 l)",command=Fritz_Limo_gross, height=1, width=30, activebackground="green")
button_3.grid(column=1, row=9)
button_3 = Tkinter.Button(text="Fritz-limo / Fritz-kola klein (0.33 l)",command=Fritz_Limo_klein, height=1, width=30, activebackground="green")
button_3.grid(column=1, row=10)
button_3 = Tkinter.Button(text="IRN BRU (0.33 l)",command=IRN_BRU, height=1, width=30, activebackground="green")
button_3.grid(column=1, row=11)
button_3 = Tkinter.Button(text="Krombacher Radler",command=krombacher_radler, height=1, width=30, activebackground="green")
button_3.grid(column=1, row=12)
button_3 = Tkinter.Button(text="Monster Energy Drink (0.50 l)",command=Monster, height=1, width=30, activebackground="green")
button_3.grid(column=1, row=13)
button_3 = Tkinter.Button(text="Mountain Dew (0.50 l)",command=Mountain_Dew, height=1, width=30, activebackground="green")
button_3.grid(column=1, row=14)
button_3 = Tkinter.Button(text="Ratsherrn New Era (0.33 l)",command=Ratsherrn_new_era, height=1, width=30, activebackground="green")
button_3.grid(column=1, row=15)
button_3 = Tkinter.Button(text="Ratsherrn Pilsener (0.33 l)",command=Ratsherrn_pilsener_klein, height=1, width=30, activebackground="green")
button_3.grid(column=1, row=16)
button_3 = Tkinter.Button(text="Red Bull klein (0.25 l)",command=red_bull_klein, height=1, width=30, activebackground="green")
button_3.grid(column=1, row=17)
button_3 = Tkinter.Button(text="Red Bull groß (0.355 l)",command=red_bull_gross, height=1, width=30, activebackground="green")
button_3.grid(column=1, row=18)
button_3 = Tkinter.Button(text="Rothaus Pils \n Tannenzäpfle (0.33 l)",command=rothaus_tannenzaepfle, height=2, width=30, activebackground="green")
button_3.grid(column=1, row=19)

####################################
#Zweite Spalte, Preise:            #
####################################
label_2 = Tkinter.Label(text=" Getränkekasse ", borderwidth=2, relief="groove", background="green", foreground="white")
label_2.grid(column=2, row=1 )
####################################
#Preise:                           #
####################################
label_3 = Tkinter.Label(text="")
label_3.grid(column=2, row=2 )
label_6 = Tkinter.Label(text="<-- 1.75€")
label_6.grid(column=2, row=3 )
label_4 = Tkinter.Label(text="<-- 0.80€", height=3)
label_4.grid(column=2, row=4 )
#label_5 = Tkinter.Label(text="<-- 0.85€")
#label_5.grid(column=2, row=4 )
#label_6 = Tkinter.Label(text="<-- 0.55€")
#label_6.grid(column=2, row=5 )
label_6 = Tkinter.Label(text="<-- 1.00€")
label_6.grid(column=2, row=5 )
#label_6 = Tkinter.Label(text="<-- 0.60€")
#label_6.grid(column=2, row=7 )
label_6 = Tkinter.Label(text="<-- 0.90€")
label_6.grid(column=2, row=6 )
label_6 = Tkinter.Label(text="<-- 0.70€")
label_6.grid(column=2, row=7 )
label_6 = Tkinter.Label(text="<-- 1.40€")
label_6.grid(column=2, row=8 )
label_6 = Tkinter.Label(text="<-- 1.55€")
label_6.grid(column=2, row=9 )
label_6 = Tkinter.Label(text="<-- 1.10€")
label_6.grid(column=2, row=10 )
label_6 = Tkinter.Label(text="<-- 1.40€")
label_6.grid(column=2, row=11 )
label_6 = Tkinter.Label(text="<-- 0.80€")
label_6.grid(column=2, row=12 )
label_6 = Tkinter.Label(text="<-- 2.00€")
label_6.grid(column=2, row=13 )
label_6 = Tkinter.Label(text="<-- 1.05€")
label_6.grid(column=2, row=14 )
label_6 = Tkinter.Label(text="<-- 1.60€")
label_6.grid(column=2, row=15 )
label_6 = Tkinter.Label(text="<-- 0.85€")
label_6.grid(column=2, row=16 )
label_6 = Tkinter.Label(text="<-- 1.55€")
label_6.grid(column=2, row=17 )
label_6 = Tkinter.Label(text="<-- 2.05€")
label_6.grid(column=2, row=18 )
label_6 = Tkinter.Label(text="<-- 1.05€", height=2)
label_6.grid(column=2, row=19 )

#############################################
#Dritte Spalte, Übersicht der Ausgaben:     #
#############################################
label_7 = Tkinter.Label(text="Übersicht der Ausgaben:", borderwidth=2, relief="groove")
label_7.grid(column=3, row=1)
#############################################
#Übersicht nach Personen/Karten:            #
#############################################
label_1 = Tkinter.Label(text="Stammesinterne:", borderwidth=2, relief="groove")
label_1.grid(column=3, row=3)
button_4 = Tkinter.Button(text="macu",command=db_abfrage_person_eins, height=1, width=20, activebackground="green")
button_4.grid(column=3, row=13)
button_6 = Tkinter.Button(text="apito",command=db_abfrage_person_zwei, height=3, width=20, activebackground="green")
button_6.grid(column=3, row=4)
button_4 = Tkinter.Button(text="ganti",command=db_abfrage_person_drei, height=1, width=20, activebackground="green")
button_4.grid(column=3, row=6)
button_6 = Tkinter.Button(text="jention",command=db_abfrage_person_vier, height=1, width=20, activebackground="green")
button_6.grid(column=3, row=12)
button_4 = Tkinter.Button(text="hugin",command=db_abfrage_person_fuenf, height=1, width=20, activebackground="green")
button_4.grid(column=3, row=9)
button_6 = Tkinter.Button(text="elon",command=db_abfrage_person_sechs, height=1, width=20, activebackground="green")
button_6.grid(column=3, row=5)
button_4 = Tkinter.Button(text="spicy",command=db_abfrage_person_sieben, height=1, width=20, activebackground="green")
button_4.grid(column=3, row=15)
button_6 = Tkinter.Button(text="saira",command=db_abfrage_person_acht, height=1, width=20, activebackground="green")
button_6.grid(column=3, row=14)
button_4 = Tkinter.Button(text="Jan",command=db_abfrage_person_neun, height=1, width=20, activebackground="green")
button_4.grid(column=3, row=11)
button_6 = Tkinter.Button(text="hrãva",command=db_abfrage_person_zehn, height=1, width=20, activebackground="green")
button_6.grid(column=3, row=8)
button_6 = Tkinter.Button(text="guamo",command=db_abfrage_person_elf, height=1, width=20, activebackground="green")
button_6.grid(column=3, row=7)
button_6 = Tkinter.Button(text="isil",command=db_abfrage_person_zwoelf, height=1, width=20, activebackground="green")
button_6.grid(column=3, row=10)
label_1 = Tkinter.Label(text="Stammesexterne:", borderwidth=2, relief="groove")
label_1.grid(column=3, row=16)
button_6 = Tkinter.Button(text="Michel (MLK)",command=db_abfrage_person_dreizehn, height=1, width=20, activebackground="green")
button_6.grid(column=3, row=17)
#button_5 = Tkinter.Button(text="Testkarte Eins",command=db_abfrage_karte_eins, height=1, width=20, activebackground="green")
#button_5.grid(column=3, row=13)
#button_5 = Tkinter.Button(text="Testkarte Zwei",command=db_abfrage_karte_zwei, height=1, width=20, activebackground="green")
#button_5.grid(column=3, row=14)
#button_5 = Tkinter.Button(text="Karte Drei",command=db_abfrage_karte_drei, height=1, width=20, activebackground="green")
#button_5.grid(column=3, row=15)
#button_5 = Tkinter.Button(text="Karte Vier",command=db_abfrage_karte_vier, height=1, width=20, activebackground="green")
#button_5.grid(column=3, row=16)
#button_5 = Tkinter.Button(text="Karte Fünf",command=db_abfrage_karte_fuenf, height=1, width=20, activebackground="green")
#button_5.grid(column=3, row=17)

#########################################################
#Vierte Spalte, Ausgaben des letzten Monats:            #
#########################################################
label_7 = Tkinter.Label(text="Ausgaben des letzten Monats:", borderwidth=2, relief="groove")
label_7.grid(column=4, row=1)
#########################################################
#Ausgaben des letzten Monats für jede Person/Karte:     #
#########################################################
label_1 = Tkinter.Label(text="Stammesinterne:", borderwidth=2, relief="groove")
label_1.grid(column=4, row=3)
button_5 = Tkinter.Button(text="macu | 1 Monat",command=db_abfrage_person_eins_monat, height=1, width=20, activebackground="green")
button_5.grid(column=4, row=13)
button_5 = Tkinter.Button(text="apito | 1 Monat",command=db_abfrage_person_zwei_monat, height=3, width=20, activebackground="green")
button_5.grid(column=4, row=4)
button_4 = Tkinter.Button(text="ganti | 1 Monat",command=db_abfrage_person_drei_monat, height=1, width=20, activebackground="green")
button_4.grid(column=4, row=6)
button_6 = Tkinter.Button(text="jention | 1 Monat",command=db_abfrage_person_vier_monat, height=1, width=20, activebackground="green")
button_6.grid(column=4, row=12)
button_4 = Tkinter.Button(text="hugin | 1 Monat",command=db_abfrage_person_fuenf_monat, height=1, width=20, activebackground="green")
button_4.grid(column=4, row=9)
button_6 = Tkinter.Button(text="elon | 1 Monat",command=db_abfrage_person_sechs_monat, height=1, width=20, activebackground="green")
button_6.grid(column=4, row=5)
button_4 = Tkinter.Button(text="spicy | 1 Monat",command=db_abfrage_person_sieben_monat, height=1, width=20, activebackground="green")
button_4.grid(column=4, row=15)
button_6 = Tkinter.Button(text="saira | 1 Monat",command=db_abfrage_person_acht_monat, height=1, width=20, activebackground="green")
button_6.grid(column=4, row=14)
button_4 = Tkinter.Button(text="Jan | 1 Monat",command=db_abfrage_person_neun_monat, height=1, width=20, activebackground="green")
button_4.grid(column=4, row=11)
button_6 = Tkinter.Button(text="hrãva | 1 Monat",command=db_abfrage_person_zehn_monat, height=1, width=20, activebackground="green")
button_6.grid(column=4, row=8)
button_6 = Tkinter.Button(text="guamo | 1 Monat",command=db_abfrage_person_elf_monat, height=1, width=20, activebackground="green")
button_6.grid(column=4, row=7)
button_6 = Tkinter.Button(text="isil | 1 Monat",command=db_abfrage_person_zwoelf_monat, height=1, width=20, activebackground="green")
button_6.grid(column=4, row=10)
label_1 = Tkinter.Label(text="Stammesexterne:", borderwidth=2, relief="groove")
label_1.grid(column=4, row=16)
button_6 = Tkinter.Button(text="Michel (MLK) | 1 Monat",command=db_abfrage_person_dreizehn_monat, height=1, width=20, activebackground="green")
button_6.grid(column=4, row=17)
#button_5 = Tkinter.Button(text="Testkarte Eins | 1 Monat",command=db_abfrage_karte_eins_monat, height=1, width=20, activebackground="green")
#button_5.grid(column=4, row=13)
#button_5 = Tkinter.Button(text="Testkarte Zwei | 1 Monat",command=db_abfrage_karte_zwei_monat, height=1, width=20, activebackground="green")
#button_5.grid(column=4, row=14)
#button_5 = Tkinter.Button(text="Karte Drei | 1 Monat",command=db_abfrage_karte_drei_monat, height=1, width=20, activebackground="green")
#button_5.grid(column=4, row=15)
#button_5 = Tkinter.Button(text="Karte Vier | 1 Monat",command=db_abfrage_karte_vier_monat, height=1, width=20, activebackground="green")
#button_5.grid(column=4, row=16)
#button_5 = Tkinter.Button(text="Karte Fünf | 1 Monat",command=db_abfrage_karte_fuenf_monat, height=1, width=20, activebackground="green")
#button_5.grid(column=4, row=17)

###########################################
#Fünfte Spalte, Extras:                   #
###########################################
label_8 = Tkinter.Label(text="Extras:", borderwidth=2, relief="groove")
label_8.grid(column=5, row=1)
###########################################
#Extras:                                  #
###########################################
#Wer hat die meisten Getränke getrunken?
button_5 = Tkinter.Button(text="Wer hat die meisten Getränke getrunken?",command=db_abfrage_getraenke_menge, height=1, width=35, activebackground="green")
button_5.grid(column=5, row=3)
#Welches Getränk wird am meisten getrunken?
button_5 = Tkinter.Button(text="Was wird am meisten getrunken?",command=db_abfrage_topseller_menge, height=3, width=35, activebackground="green")
button_5.grid(column=5, row=4)
#Welche Getränke sind noch da?
button_5 = Tkinter.Button(text="Welche Getränke sind noch da?",command=db_abfrage_bestand, height=1, width=35, activebackground="green")
button_5.grid(column=5, row=5)

############################################
#Badge einbinden:                          #
############################################
photo = PhotoImage(file='badge.gif')
label = Tkinter.Label(image = photo)
label.grid(column=5, row=6, rowspan=11)
#photo.grid(column=5, row=6)

###########################################
#Sechste Spalte, Anleitung:               #
###########################################
label_8 = Tkinter.Label(text="Anleitung:\n \n 1. Wähle ein Getränk! \n 2. Halte deinen RFID-Chip vor das Lesegerät unten \n 3. Du bekommst eine Nachricht, wenn das Getränk auf dich gebucht wurde \n 4. Lehn dich zurück und lass dir dein Getränk schmecken! :-)", borderwidth=3, relief="solid")
label_8.grid(column=5, row=18, rowspan=5)

###########################################
#Anmerkungen:                             #
###########################################
label_8 = Tkinter.Label(text="", borderwidth=2)
label_8.grid(column=2, row=20)
label_8 = Tkinter.Label(text="*Preise inkl. Pfand*", borderwidth=2, relief="ridge")
label_8.grid(column=2, row=20)
label_8 = Tkinter.Label(text="Zeitangaben bei der Buchungsabfrage \n erfolgen in Coordinated Universal Time (UTC). \n Mitteleuropäische Zeit (MEZ) = +1 Stunde. \n Mitteleuropäische Sommerzeit (MESZ) = +2 Stunden.", borderwidth=2, relief="ridge")
label_8.grid(column=3, columnspan=2, row=19, rowspan=2)


Tkinter.mainloop()

