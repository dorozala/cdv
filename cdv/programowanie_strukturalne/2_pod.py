tekst = "Anna, pawel, tomek"

tab = tekst.split(", ")
print(tekst)
print(tab)
print(type(tab)) #lista

imie1 = tab[0]
print(imie1) #Anna

print("Twoje imie: " + imie1)

imieDuze = imie1.upper()
print(imieDuze)

imieMale = imie1.lower()
print(imieMale)

#sprawdzenie zawartosci
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc) #true lub false
print(type(zawartosc)) #bool

nazwisko = ""
print(nazwisko.isalpha()) #false

imie = "Julia"
print("\nDane uzytkownika\nMasz na imie:" , imie)

text1 = "Jan\n"
text2 = "Nowak"
print(text1 + text2)


text1 = text1.rstrip()
print(text1 + text2)
print(text1 + " " + text2)

#wyswietlanie lancuchow znakow
#wszystkie wersje pythona
text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowsze wersje Pythona 2.6
text = "{0}, Java i {1}".format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisanie danych
rok = 2019
miesiac = "marzec"
dzien = 25

print("Data: ", end="")
print(dzien, miesiac, rok)


print("Data: ", end="")
print(dzien, miesiac, rok, sep="-")















print()
