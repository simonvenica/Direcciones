def buscar_altura(lista_direccion): #Busca la altura, devuelve su posicion en la lista de palabras

	contador_numeros = 0
	for palabra in lista_direccion: #Si la direccion tiene una sola palabra que sean digitos, la considera como altura y termina el proceso devolviendo su posicion.
		if palabra.replace("n","").isdigit(): #Reemplaza la "n" por los casos que viene por ejemplo "Avellaneda N533" (se usa varias veces adelante)
			contador_numeros = contador_numeros + 1
			numero = palabra
	if contador_numeros == 1:
		posicion_altura = lista_direccion.index(numero)
		return posicion_altura
	
		
	
	bool_primera_palabra = True
	palabra_anterior = "" #En esta variable guarda la palabra anterior para comprobar que no este en la lista de palabras que puedan seguirle un numero sin ser la altura (ej: calle 12, avenida 5)
	
	for palabra in lista_direccion:
		if bool_primera_palabra: #Guarda la primera palabra y continua con la segunda (la primera nunca puede ser la altura)
			primera_palabra = palabra 
			palabra_anterior = palabra 
			bool_primera_palabra = False
			continue
			
		if palabra.replace("n","").isdigit() and not palabra_anterior
		
		
		
		

def proceso_direcciones():
	direccion = raw_input("Direccion a separar: ")
	direccion = direccion.lower()
	lista_direccion = domicilio.split(" ")
	
	altura = buscar_altura(lista_direccion)
	
	
	
	
	

			
		
		
	
	

	
	
	
	
	
	
	
	
def main():
	proceso_direcciones()
	
	
	

	
	
main()