from abc import ABC, abstractmethod # abstract class module

class Czlowiek(ABC): # base abstract class
    @classmethod
    @abstractmethod
    def getOpiekun(cls): # pure virtual / abstract function
        pass

    def __init__(self, imie = 'brak', nazwisko = 'brak', pesel = 'brak', email = 'brak'): # constructor

        # protected variables:
        self._imie = imie
        self._nazwisko = nazwisko
        self._pesel = pesel
        self._email = email


    # public methods:
    def getPesel(self):
        return self._pesel


    def getImie(self):
        return self._imie


    def getNazwisko(self):
        return self._nazwisko


    def getEmail(self):
        return self._email
