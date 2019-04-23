entrada = 10

def retrocontador(e):
	print("{}, ".format(e), end="")
	if e > 0:
		retrocontador(e-1)

retrocontador(entrada)

def sumatorio(n):
	if n > 0:
		return n + sumatorio(n-1)
	return n

print(sumatorio(10))

def factorial(n):
	if n > 0:
		return n*factorial(n-1)
	return 1

n = 4
print("El factorial de {} es: {}".format(n, factorial(n)))