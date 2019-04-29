#petla for

colors = ['red','green','blue','magenta']
print(colors)
print(type(colors))

for color in colors:
    print(color)

print('\n')

#wypisz tekst
string = 'cdv - uczelnia ludzi ciekawych'
for str in string:
    print(str,end=" ")
print()
#wypisz liczby od 1 do 10
for number in range(1, 11):
    print(number,end=" ")

print()

#wypisz elementy z listy do momentu wartosci 'end', 'q', 'quit'

lista = ['red','end','green','quit','blue','magenta','q']
for list in lista:
    print(list)
