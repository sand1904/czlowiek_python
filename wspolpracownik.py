from czlowiek import Czlowiek

class Wspolpracownik(Czlowiek):
    def __init__(self, imie = 'brak', nazwisko = 'brak', pesel = 'brak', email = 'brak', wspolid = -1): # constructor
        Czlowiek.__init__(self, imie, nazwisko, pesel, email) # inheritance of parent's class constructor

        self.wspolid = wspolid # numer id pracownika odpowiedzialnego za wspolprace


    def getOpiekun(self): # virtual function override
        return self.wspolid
