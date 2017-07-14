import libreria_direcciones



def limpiar_texto(texto) #Limpia un texto de imperfecciones recurrentes y lo devuelve en minusculas
	texto = texto.lower()
	texto = texto.strip(" ")
	while "  " in texto:
		texto.replace("  "," ")


def buscar_altura(lista_direccion): #Busca la altura, devuelve su posicion en la lista de palabras, si no la encuentra devuelve 0

	contador_numeros = 0
	for palabra in lista_direccion: #Si la direccion tiene una sola palabra que sean digitos, la considera como altura y termina el proceso devolviendo su posicion.
		if palabra.replace("n","").isdigit(): #Reemplaza la "n" por los casos que viene por ejemplo "Avellaneda N533" (se usa varias veces adelante)
			contador_numeros = contador_numeros + 1
			numero = palabra
	if contador_numeros == 1:
		posicion_altura = lista_direccion.index(numero)
		return posicion_altura
	
	if contador_numeros == 0:
		return 0
	
	
	"""Si no encontró la altura hasta ahora, prueba con otro proceso"""
	
	
	bool_primera_palabra = True
	palabra_anterior = "" #En esta variable guarda la palabra anterior para comprobar que no este en la lista de palabras que puedan seguirle un numero sin ser la altura (ej: calle 12, avenida 5)
	for palabra in lista_direccion:
		if bool_primera_palabra: #Guarda la primera palabra y continua con la segunda (la primera nunca puede ser la altura)
			palabra_anterior = palabra 
			bool_primera_palabra = False
			continue
		if palabra.replace("n","").isdigit() and not palabra_anterior in libreria_direcciones.lista_primera_palabra:
			
		
		
		
		

def proceso_direcciones():
	direccion = raw_input("Direccion a separar: ")
	
	direccion = limpiar_texto(direccion)

	lista_direccion = direccion.split(" ")
	
	altura = buscar_altura(lista_direccion)
	
	print altura
	
	
	

	
def main():
	proceso_direcciones()
	
	
	

	
	
main()