class gerecht:

    def __init__(self,naam, omschrijving, prijs):
        self.naam = naam
        self.omschrijving = omschrijving
        self.prijs = prijs
    def __str__(self):
        return "Naam: {}\nOmschrijving {}\t\t\t€ {}".format(self.naam,self.omschrijving,self.prijs)



