from abc import ABC, abstractmethod # abstract class module

class Czlowiek(ABC): # base abstract class
    @classmethod
    @abstractmethod
    def getOpiekun(cls): # pure virtual / abstract function
        pass

    def __init__(self, imie = 'brak', nazwisko = 'brak', pesel = 'brak', email = 'brak'): # constructor
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.email = email

    def getPesel(self):
        return self.pesel

    def getImie(self):
        return self.imie

    def getNazwisko(self):
        return self.nazwisko

    def getEmail(self):
        return self.email
