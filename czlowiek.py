from abc import ABC, abstractmethod # abstract class module

class Czlowiek(ABC): # abstract class
    @classmethod
    @abstractmethod
    def getOpiekun(cls): # pure virtual / abstract function
        pass

    def __init__(self, imie, nazwisko, pesel, email): # constructor
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
