class Perro():
	def __init__(self, n, e, p):
		self.nombre = n
		self.edad = e
		self.peso = p

	def ladrar(self):
		if self.peso >= 8:
			print('GUAU, GUAU!')
		else:
			print('guau, guau!')

	def __str__(self):
		return ("Soy el perro {}, con {} años y peso {} kilos.".format(
			self.nombre, self.edad, self.peso))

salchicho = Perro('Salchicho',3,12)
print(salchicho.nombre)
salchicho.ladrar()
lola = Perro('Lola', 8, 1.5)
lola.ladrar()
miko = Perro('Miko', 8, 3)
print(salchicho)
