from czlowiek import Czlowiek

class Pracownik(Czlowiek):
    def __init__(self, imie = 'brak', nazwisko = 'brak', pesel = 'brak', email = 'brak', umowa = 'brak',
                 pracid = -1, szefid = -1): # constructor
        Czlowiek.__init__(self, imie, nazwisko, pesel, email) # inheritance of parent's class constructor

        # protected variables:
        self._umowa = umowa
        self._pracid = pracid
        self._szefid = szefid


    # public methods:
    def getDataUmowy(self):
        return self._umowa


    def getID(self):
        return self._pracid


    def getOpiekun(self):# virtual function override
        return self._szefid
