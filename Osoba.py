class Osobę:
    def __init__(self,name, surname,age):
        self.name=name
        self.surname=surname
        self.age=age
osoba1 = Osobę("Antek","Alibek","18")
print(osoba1.name)