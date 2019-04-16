programowanie = ['Python', 'PHP', 'C#', 'JS', 'Java']
print(programowanie)
print(type(programowanie))

pierwszy = programowanie[0]
print(pierwszy)

trzyelementy = programowanie[0:3]
print(trzyelementy)

ostatnielement = programowanie[-1]
print(ostatnielement)

#Dodanie nowego elementu na koniec listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

#Zliczanie elementow w liscie
ile = programowanie.count('Python')
print(ile)

#Ilosc elementow
iloscelem = len(programowanie)
print(iloscelem)

#Połączenie list
innejezyki = ['C','C++']
programowanie.extend(innejezyki)
print(programowanie)

#Czyszczenie list
nowa = programowanie
print('Lista nowa:' ,end="")
print(nowa)
nowa.clear()
print('Lista nowa:' ,end="")
print(nowa)
print(programowanie)
