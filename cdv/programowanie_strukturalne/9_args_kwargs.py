import os
def wyswietl(num1, num2):
    print(f'liczba 1: {num1}')
    print(f'liczba 2: {num2}')

wyswietl(3,4)

#############  args ###############

def wyswietlArgs(num1, *args):
    print(f'\nliczba 1: {num1}')
    for i in args:
        print(f'nastepna wartosc: {i}')

wyswietlArgs(1, 12, 1000, 211, 2)

###################

imiona = ['anna','jan','pawel']
wyswietlArgs(imiona)
wyswietlArgs(*imiona)
os.system('cls')

#################### kwargs ####################
def pracownik(**kwargs):
    for key, val in kwargs.items():
        print(f'klucz {key}, wartosc {val}')

pracownik1 = {
    'imie':'Janusz',
    'nazwisko':'Kowalski',
    'wiek':21,
    'umowaOprace': True
}

pracownik(**pracownik1)
