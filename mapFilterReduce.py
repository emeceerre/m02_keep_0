lista = [1, 3,-1, 15, 9]
lista_dobles = map(lambda x: x*2, lista)
print('Lista de dobles: ', list(lista_dobles))

lista_pares = filter(lambda x: x%2==0, lista)
print('Lista de pares: ', list(lista_pares))

for va in lista_dobles:
	print('holi', va)