def sumatodos(limitTo):
	resultado = 0
	for i in range(0, limitTo+1):
		resultado += i
	return resultado

def sumatodosLosCuadrados(limitTo):
	resultado = 0
	for i in range(limitTo):
		resultado += i*i
	return resultado

print(sumaTodos(100))
print(sumatodosLosCuadrados(3))
