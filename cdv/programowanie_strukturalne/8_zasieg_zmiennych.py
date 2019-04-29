#Zasieg zmiennych, zmienne lokalne i globalne

#Precyzja liczby (zaokrąglenie do 3 miejsc po przecinku liczby 5: 5.000)

x = "{0:.3f}".format(5)
print(x)

def plnToChf(value):
    kursChf = 3.7913
    iloscChf = value / kursChf
    iloscChf = '{0:.4f}'.format(iloscChf)
    print(iloscChf)

plnToChf(1000)

'''
    Uwtorz funkcje zwracajaca ilosc euro jaka klient moze kupic za pln
'''

def euro(value):
    kurseuro = 4.2927
    ilosceuro = value / kurseuro
    ilosceuro = '{0:.0f}'.format(ilosceuro)
    print(ilosceuro)

euro(1000)

#zmienna globalna

kursUSD = 3.50
print(f'Id USD: {id(kursUSD)}')

def plnToUSD(value):
    kursUSD = 4.00
    iloscUSD = value / kursUSD
    iloscUSD = '{0:.4f}'.format(iloscUSD)
    print(f'Id USD wewnatrz funkcji: {id(kursUSD)}')
    return iloscUSD

print(f'\nKurs dolara: {kursUSD}')
pln = input('Podaj kwote PLN jaka chcesz zamienic na USD: ')
USD = plnToUSD(float(pln))
print(f'Ilosc {pln}PLN = {USD}USD')
print(f'\nKurs dolara po wywolaniu funkcji: {kursUSD}')
