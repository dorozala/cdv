def witaj():
    print('witaj Janusz!')

witaj()

def wyswietlwiek(wiek):
    print(f'Twoj wiek: {wiek}')

wyswietlwiek(22)

def iloczyn(a, b):
    return a*b

print(iloczyn(3,4))

def iloraz(a, b):
    return a/b

iloraz1 = iloraz(3,4)
print(iloraz1)
print(type(iloraz1))

print(iloraz(b=5, a=2))

'''
uzytkownik podaje z klawiatury:
marka,model,pojemnosc,predkoscmax
utworz funkcje ktora pobierze dane od uzytkownika i przypisze do slownika
utworz druga funkcje wyswietlajaca dane w formacie:
marka:...
model:
pojemnosc:
predkosc maksymalna:
'''


marka = input('Podaj marke: ')
model = input('Podaj model: ')
pojemnosc: input('Podaj pojemnosc: ')
predkosc: input('Podaj predkosc: ')

def funkcja():
    auto = {
    'marka':marka,
    'model':model,
    'pojemnosc':pojemnosc,
    'predkosc':predkosc
    }

funkcja()
