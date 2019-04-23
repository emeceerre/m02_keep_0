import functools

lista = [1, 3,-1, 15, 9]
lista_dobles = map(lambda x: x*2, lista)
print('Lista de dobles: ', list(lista_dobles))

lista_pares = filter(lambda x: x%2==0, lista)
print('Lista de pares: ', list(lista_pares))

def SumatorioDoble(l):
	resultado = 0
	for valor in l:
		resultado += valor*2
	return resultado

def ProductoTotal(l):
	resultado = 1
	for valor in l:
		resultado *= valor
	return resultado

lista = [1, 3, -1, 15, 9]

sumatorio = functools.reduce(lambda x, y: x+y, lista)

# creo una copia de la lista
l = lista[:]
# añado el neutro de la suma en la posición cero
l.insert(0,0)
sumatorioDobles = functools.reduce(lambda x, y: x + y*2, l)
sumatorioDoblesClasico = SumatorioDoble(lista)

print(sumatorio)
print(sumatorioDobles)
print(sumatorioDoblesClasico)