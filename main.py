from firma import Firma

def main():
    f = Firma()

    f.wczytaj('pracownicy.txt', 'wspolpracownicy.txt')


if __name__ == '__main__':
    main()