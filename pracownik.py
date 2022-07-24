from czlowiek import Czlowiek

class Pracownik(Czlowiek):
    def __init__(self, imie = 'brak', nazwisko = 'brak', pesel = 'brak', email = 'brak', umowa = 'brak',
                 pracid = -1, szefid = -1): # constructor
        Czlowiek.__init__(self, imie, nazwisko, pesel, email) # inheritance of parent's class constructor

        self.umowa = umowa
        self.pracid = pracid
        self.szefid = szefid


    def getDataUmowy(self):
        return self.umowa


    def getID(self):
        return self.pracid


    def getOpiekun(self):# virtual function override
        return self.szefid
