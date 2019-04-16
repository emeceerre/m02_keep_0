def maxi(*l):
	if len(l) == 0:
		return 0
	m = l[0]
	for num in l:
		if num > m:
			m = num
	return m

def mini(*l):
	if len(l) == 0:
		return 0
	m = l[0]
	for num in l:
		if num < m:
			m = num
	return m

def media(*l):
	if len(l) == 0:
		return 0
	suma = 0
	for valor in l:
		suma += valor
	return suma/len(l)

funciones = {'max': maxi, 'min': mini, 'med': media}
def returnF(nombre):
	nombre = nombre.lower()
	if nombre in funciones.keys():
		return funciones[nombre]
	return None

f = returnF('max')
print(f(1,3,-1,15,9))
f = returnF('min')
print(f(1,3,-1,15,9))
# o tambié se puede llamar así
print(returnF('med')(1,3,-1,15,9))