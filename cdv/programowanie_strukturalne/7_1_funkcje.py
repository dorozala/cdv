

def show(name):
    print(f'Przed modyfikacja: {name}')
    name[0] = 'Beata'
    name[1] = 'Barbara'
    name[2] = 'Bogdan'
    print(f'Po modyfikacja: {name}')
    print(f'Po modyfikacja: {id(name)}')

data=['Anna','Agnieszka','Andrzej']

print(f'Przed wywolaniem funkcji show: {data}')
print(f'Id obiektu: {id(data)}')

show(data)

print(f'Po wywolaniu funkcji show: {data}')

######################

data1 = {
    0:'Artur',
    1:'Andrzej'
}

print(f'\nPrzed wywolaniem funkcji show:{data1}')
show(data1)

#Przekazywanie argumentow przez wartosc
print('\n###########Przekazywanie argumentow przez wartosc\n')

def show1(city):
    print(f'Przed modyfikacja: {city}')
    city[0] = 'Berlin'
    city[1] = 'Bukareszt'
    print(f'Po modyfikacja: {city}')
    print(f'Po modyfikacja: {id(city)}')

miasto = ['Poznan','Gniezno']
print(f'Przed wywolaniem funkcji show1: {miasto}')
print(f'Id obiektu: {id(miasto)}')
show1(list(miasto))
print(f'Po wywolaniu funkcji show1: {miasto}')


############slownik#############
print('\n###########Przekazywanie argumentow przez wartosc slownik\n')
miasto1 = {0:'Poznan',1:'Gniezno'}
print(f'Przed wywolaniem funkcji show1: {miasto1}')
print(f'Id obiektu: {id(miasto1)}')
show1(dict(miasto1))
print(f'Po wywolaniu funkcji show1: {miasto1}')
