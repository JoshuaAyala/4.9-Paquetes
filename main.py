from package import operaciones

def goBack():
	goBackV = int(input("¿Quieres regresar al menú?\n\n[1] Sí.\n[2] No.\n\n>: "))
	if(goBackV == 1):
		menu()
	else:
		exit()

def menu():
	eleccion = int(input("Elige una opción:\n[1] Suma.\n[2] Resta.\n\n[0] Salir.\n\n>: "))
	if(eleccion == 1):
		x = int(input("Introduce un valor: "))
		y = int(input("Introduce un valor: "))
		print("El resultado es:", operaciones.suma(x,y,0))
		goBack()
	elif(eleccion == 2):
		x = int(input("Introduce un valor: "))
		y = int(input("Introduce un valor: "))
		print("El resultado es:", operaciones.resta(x,y,0))
		goBack()
	else:
		exit()

menu()