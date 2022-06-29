from persoon_class import persoon
from boek_class import boek

class uitlening:
    def __init__(self,id,boek,persoon):
        self.id = id
        self.boek = boek
        self.persoon = persoon

    def __str__(self):
        return "ID:\t{}\nBoek:\t{}\nPersoon:\t{}".format(self.id,self.boek.titel,self.persoon.naam)

