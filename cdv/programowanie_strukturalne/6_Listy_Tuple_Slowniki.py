#listy
imiona = ['Julia','Anna','Krystyna']
print(type(imiona))
imiona.append('Janusz')
print(imiona)
print(len(imiona))

#Tuple
nazwisko = ('Kowalski','Nowak')
print(type(nazwisko))
print(nazwisko)

#słowniki
osoba = {
    'imie':'Julia',
    'nazwisko':'Nowak',
    'wiek':23
}
print(osoba)
print(type(osoba))
print(osoba['nazwisko'])
print(osoba.keys())
print(osoba.get('wzrost','Brak danych'))
print(osoba.get('imie','Brak danych'))
