class Kalkulator:
    pass

class Odejmowanie:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def odejmij(self):
        return self.a - self.b

class Dodawanie(Odejmowanie):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dodaj(self):
        return self.a + self.b


class Mnożenie:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pomnóż(self):
        return self.a * self.b

class Dzielenie:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def podziel(self):
        if self.b != 0:
            return self.a / self.b
        else:
            print("Błąd: Nie można dzielić przez zero.")
            return None

# Example usage:
obiekt1 = Odejmowanie(5,3)
wynik = obiekt1.odejmij()
print(wynik)