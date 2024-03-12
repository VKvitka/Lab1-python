class ZwirzeDomowe:
    pass
class Zwiezęta:
    def __init__(self,imię, gatunek):
        self.imię = imię
        self.gatunek = gatunek
        
    def przedstaw_sie(self):
        return f"Jestem {self.imię}, jestem {self.gatunek}."
kot = Zwiezęta("Mrucek", "kot")
pies = Zwiezęta("Burek", "pies")
chomik = Zwiezęta("Bączek", "chomik")
print(kot.przedstaw_sie())
print(pies.przedstaw_sie())
print(chomik.przedstaw_sie())
