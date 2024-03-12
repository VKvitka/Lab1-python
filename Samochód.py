class Samochod:
    def __init__(self,marka,model,rok,przebieg):
        self.marka = marka
        self.model = model
        self.rok = rok
        self.przebieg = przebieg
samochod1 = Samochod("Fiat","Punto","2008","230000")
samochod2 = Samochod("BMW","M3","2016","75000")
samochod3 = Samochod("Infiniti","Q50","2016","135000")
samochod4 = Samochod("Audi","RS6","2020","30000")
samochod5 = Samochod("Mercedes-Benz","E63","2014","250000")
print(samochod1.marka, samochod1.model, samochod1.rok, samochod1.przebieg)
print(samochod2.marka, samochod2.rok, samochod2.przebieg, samochod2.model)
