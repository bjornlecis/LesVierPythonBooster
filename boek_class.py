class boek:
    def __init__(self,id,titel,auteur):
        self.id = id
        self.titel = titel
        self.auteur = auteur

    def __str__(self):
        return "ID {} titel {} auteur {}".format(self.id,self.titel,self.auteur)

