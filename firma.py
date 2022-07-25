from pracownik import Pracownik
from wspolpracownik import Wspolpracownik

class Firma:
    def __init__(self): # constructor
        # private variables:
        self.__file1_list = None
        self.__file2_list = None


    # public methods:
    def wczytaj(self, fileprac, filewspolprac): # reading data from txt files
        file1_list = [] # list with file1 contents [ list of lists line by line ]
        file2_list = [] # list with file2 contents

        with open(fileprac, encoding="utf8") as file1:  # open first file
            for line in file1: # iterate line by line through file
                prac_list = file1.readline() # reading line from txt to variable

                file1_list.append(prac_list)

        with open(filewspolprac, encoding="utf8") as file2:  # open second file
            for line in file2: # iterate line by line through file
                prac_list = file2.readline() # reading line from txt to variable

                file2_list.append(prac_list)

        # make file lists usable for other methods in this class
        self.__file1_list = file1_list
        self.__file2_list = file2_list

        # closing files
        file1.close()
        file2.close()


    def urodziny(self, date1: int, date2: int): # creates a list with data of people that have birthday on day passed in the argument
        # month, day

        uro_list = [] # list of data of people that have birthday

        # combine date1 and  int variables into 1 string
        if date1 > -1 and date1 < 10:
            s_date = '0' + str(date1) + '-' + str(date2)
        else:
            s_date = str(date1) + '-' + str(date2)


        for i in self.__file1_list: # iterate through file 1 contents list
            if s_date in self.__file1_list:
                uro_list.append(i)

        for i in self.__file2_list: # iterate through file 2 contents list
            if s_date in self.__file2_list:
                uro_list.append(i)
