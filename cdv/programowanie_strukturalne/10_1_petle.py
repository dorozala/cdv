#Petle zadania

'''
podaj wartosc początkowa i koncowa ktora bedzie wpisana w porzadku malejacym
uzytkownik podaje x i y i posortowac w porzadku nierosnacym
'''

'''
x = int(input('podaj x: '))
y = int(input('podaj y: ')) -1

if y>x:
    pom = x
    x = y + 1
    y = pom - 1

for numer in range(x,y, -1):
    print(numer,end=" ")
'''

'''
*
**
***
****
*****
'''
#Dwie pętle
'''
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end="")
    print()
print()
'''

# 1 petla for znak i ilosc wierszy
'''
i=1
ilosc = int(input('Podaj ilosc wierszy: ')) +1
znak = input('Podaj znak: ')
print()

for i in range(1,ilosc):
    print(znak * i)
    i = i + 1
print()
'''
'''

a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
suma = a+b
if suma == 0:
    print('Proba dzielenia przez 0')
else:
    wynik = (a*a+b) / (a*a+2*a*b+b*b)
    print(wynik)
'''

##############
'''
school = 'CDV Poznan'
print()
for i in school:
    if i == 'V':
        continue
    else:
        print(i, end=" ")
print()
print()

#####################

x = 10
while x > 0:
    x = x - 1
    if x == 6:
        continue
    print(x , end =' ')
print()
print()
'''
'''
uzytkownik podaje z klawiatury haslo, jesli poda haslo: 'okon' to na
ekranie wyswietli sie komunikat : 'poprawne haslo'
uzytkownik ma na podanie hasla trzy proby jesli przekroczy ilosc prob to na
ekranie pojawi mu sie komunikat "przekroczono limi prob podania hasla"
'''
import os
os.system('cls')

password = input('Podaj haslo: ')
count = 1

while password != 'okon' and count != '3':
    count = count +1
    password = input('Podaj haslo: ')

if password == 'okon':
    print(f'Haslo odgadnieto za {count} proba' )
