print("cdv")
print(2)

#potega
potega = 2 ** 10
print(potega)

tekst = "CDV"
print(tekst * 2)

#pobieranie danych z klawiatury
imie = input()
print("Twoje imie podane z klawiatury: " + imie)

nazwisko = input()
print("Twoje imie: " + imie + ", Twoje nazwisko: " + nazwisko)

dlugosc = len(nazwisko)
print(type(nazwisko)) #string
print(type(dlugosc))  #int
print("Dlugosc nazwiska: " ,dlugosc)
dlugosc =str(dlugosc) #konwersja typu danych
print("Dlugosc nazwiska: " + dlugosc)

#uzytkownik wpisuje z klawiatury swoj wiek, wyswietl dane w formacie: Twoj wiek: ... lat

print("\nPodaj swoj wiek: ", end="")
wiek = input()
print("Twoj wiek: " + wiek + " lat")

nazwisko = "Kowalski"
pierwszyZnak = nazwisko[0]
print(pierwszyZnak)

ostatniZnak = nazwisko[len(nazwisko) -1 ]
print(ostatniZnak)
ostatniZnak = nazwisko[-1]
print(ostatniZnak)

#konwersja
x = "5"
print(type(x)) #str
x = int(x)
print(type(x)) #int

y = 4
print(type(y)) #int
y = y / 2
print(type(y)) #float
print(y) #2.0

wiek = 21
print("Twoj wiek:",wiek)
wiek = str(wiek)
print("Twoj wiek: ",wiek)

nazwisko = "Kowalski"
print(nazwisko[0]) #K
print(nazwisko[0:3]) #Kow
print(nazwisko[-2]) #k
print(nazwisko[-2:]) #ki
print(nazwisko[0:-2]) #Kowals
print(nazwisko[:-2:2]) #Kowals





















print()
