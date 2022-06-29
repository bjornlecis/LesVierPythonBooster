from bieb_class_data import lijst_personen,lijst_boeken,lijst_uitleningen
from persoon_class import persoon
from boek_class import boek
from uitlening_class import uitlening


def toon_personen():
    for x in lijst_personen:
        print(x)
def toon_boeken():
    for x in lijst_boeken:
        print(x)
def toon_uitleningen():
    for x in lijst_uitleningen:
        print(x)
def voeg_boek_toe(id,titel,auteur):
    nieuw_boek = boek(id,titel,auteur)
    lijst_boeken.append(nieuw_boek)
def voeg_persoon_toe(id,naam,geslacht):
    nieuw_persoon = persoon(id,naam,geslacht)
    lijst_personen.append(nieuw_persoon)
def voeg_uitlening_toe(id_uitlening):
    toon_boeken()
    id_boek = input("geef het id van het boek")
    for x in lijst_boeken:
        if id_boek == x.id:
            b = boek(x.id,x.titel,x.auteur)
    toon_personen()
    id_persoon = input("geef het id van de persoon")
    for x in lijst_personen:
        if id_persoon == x.id:
            p = persoon(x.id,x.naam,x.geslacht)
    nieuwe_uitlening = uitlening(id_uitlening,b,p)
    lijst_uitleningen.append(nieuwe_uitlening)

