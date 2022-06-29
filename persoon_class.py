class persoon:
    def __init__(self,id,naam,geslacht):
        self.id =id
        self.naam = naam
        self.geslacht = geslacht
    def __str__(self):
        return "ID: {} Naam: {} Geslacht {}".format(self.id,self.naam,self.geslacht)
