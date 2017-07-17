import libreria_direcciones
import sys









def ultimo_digito(lista_direccion,digito): #devuelve True en caso de que el digito sea el ultimo digito en la lista de palabras
	lista_digitos = []
	for palabra in lista_direccion:
		if palabra.replace("n","").isdigit():
			lista_digitos.append(palabra)
	if lista_digitos[len(lista_digitos)-1] == digito:
		return True
	return False
	

def limpiar_texto(texto): #Limpia un texto de imperfecciones recurrentes y lo devuelve en minusculas
	texto = texto.lower()
	texto = texto.strip(" ")
	texto = texto.strip("\n")
	while "  " in texto:
		texto.replace("  "," ")
	return texto


def buscar_altura(lista_direccion): #Busca la altura, devuelve su posicion en la lista de palabras, si no la encuentra devuelve 0

	contador_numeros = 0
	for i in range(len(lista_direccion)): #Si la direccion tiene una sola palabra que sean digitos, la considera como altura y termina el proceso devolviendo su posicion.
		palabra = lista_direccion[i]
		if palabra.replace("n","").isdigit(): #Reemplaza la "n" por los casos que viene por ejemplo "Avellaneda N533" (se usa varias veces adelante)
			contador_numeros = contador_numeros + 1
			numero = palabra
	if contador_numeros == 1:
		posicion_altura = lista_direccion.index(numero)
		return posicion_altura
	
	if contador_numeros == 0:
		return 0
	
	
	"""Si no encontro la altura hasta ahora, prueba con otro proceso"""
	
	
	palabra_anterior = "" #En esta variable guarda la palabra anterior para comprobar que no este en la lista de palabras que puedan seguirle un numero sin ser la altura (ej: calle 12, avenida 5)
	bool_primera_palabra = True
	
	for i in range(len(lista_direccion)):
		palabra = lista_direccion[i]
		if bool_primera_palabra: #Guarda la primera palabra y continua con la segunda (la primera nunca puede ser la altura)
			palabra_anterior = palabra 
			bool_primera_palabra = False
			continue
		if palabra.replace("n","").isdigit():
			if ultimo_digito(lista_direccion,palabra):
				return i
			if not palabra_anterior in libreria_direcciones.lista_primera_palabra:
				return i
		palabra_anterior = palabra
	
	return 0
			
	
def intentar_corregir_direccion(direccion): #Intenta corregir la direccion por si no encuentra la altura por un error de espacios (EJ: Santa Fe575)
	hay_digitos = False
	lista_digitos = []
	digito = ""
	for i in range(len(direccion)):
		if direccion[i].isdigit():
			hay_digitos = True
			digito = digito + direccion[i]
		if (not direccion[i].isdigit() or i == len(direccion)-1):
			if digito <> "":
				lista_digitos.append(digito)
				digito = ""
	for item in lista_digitos:
		direccion = direccion.replace(item," "+str(item)+ " ")
	direccion = limpiar_texto(direccion)
	return direccion
			

		

def proceso_direcciones():
	direccion = raw_input("Direccion a separar: ")
	direccion = limpiar_texto(direccion)
	lista_direccion = direccion.split(" ")
	
	altura = buscar_altura(lista_direccion)
	if altura == 0:
		direccion = intentar_corregir_direccion(direccion)
		lista_direccion = direccion.split(" ")
		altura = buscar_altura(lista_direccion)
	
	if altura == 0:
		print "no tiene altura capo"
		sys.exit()
	
	print "la altura es: " + str(lista_direccion[altura])
	print "su posicion es: " + str(altura)
	
	
	

	
def main():
	proceso_direcciones()
	
	
	

	
	
main()



