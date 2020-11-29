import math
from package import operaciones

def goBack():
	goBackV = int(input("¿Quieres regresar al menú?\n\n[1] Sí.\n[2] No.\n\n>: "))
	if(goBackV == 1):
		menu()
	else:
		exit()

pi = math.pi

def menu():
	eleccion = int(input("Elige una opción:\n[1] Área de Circulo.\n[2] Área de rectángulo.\n\n[0] Salir.\n\n>: "))
	if(eleccion == 1):
		radio = int(input("Introduce el valor del radio: "))
		print("El resultado es:", operaciones.circulo(radio, pi, 0))
		goBack()
	elif(eleccion == 2):
		base = int(input("Introduce el valor de la base: "))
		altura = int(input("Introduce el valor de la altura: "))
		print("El resultado es:", operaciones.rectangulo(base,altura,0))
		goBack()
	else:
		exit()

menu()