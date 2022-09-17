  #Creamos constantes de colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import random  #importamos la libreria random
import time  #importamos la libreria tiempo
# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia.

print(MAGENTA + "Bienvenido a Mi Trivia sobre Computación")
#for numero_carga in range(5, 0, -1):
 #   print(numero_carga, "...")
 #   time.sleep(1)

print("Pondremos a Prueba tus Conocimientos:\n" + RESET)
time.sleep(1)  # Espera 1 segundo antes de continuar.

# Agregaremos personalizacion a nuestros jugadores, preguntando y almacenando sus nombres en una variable.

nombre = input(BLUE + "Ingresa tu Nombre:\n")
time.sleep(0.5)  # Espera 1 segundo antes de continuar.
apellido = input("Ingresa tus Apellidos:\n")
time.sleep(0.5)  # Espera 1 segundo antes de continuar.
edad = input("Ingresa tu Edad:\n") + RESET
time.sleep(1)  # Espera 1 segundo antes de continuar.
# Es importante dar instrucciones sobre cómo jugar.
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre"y "apellido". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas

print(WHITE + "\nHola", nombre, apellido,"Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n"+ RESET)
time.sleep(1)  # Espera 1 segundo antes de continuar.

#for numero_carga in range(5, 0, -1):
  #print(numero_carga, "...")
  #time.sleep(1)

while iniciar_trivia == True:  #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = random.randint(0, 50)
  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  print(YELLOW + "comenzaras con :", puntaje, "puntos\n" + RESET)

  time.sleep(1)  # Espera 1 segundo antes de continuar.
  print(CYAN + "Pregunta 1\n")
  print("1) ¿Cuál fue la serie más vista en Netflix en el 2019?\n")
  
  print("a) Locke and Key")
  print("b) Stranger Things")
  print("c) Betty la Fea")
  print("d) Better Call Saul" + RESET)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input(GREEN + "\nTu respuesta: ")
  time.sleep(1)  # Espera 1 segundo antes de continuar.
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    if respuesta_1 == "b":
      puntaje += random.randint(5, 15)
      print("Muy bien", nombre, "!" + RESET)
    else:
      puntaje -= random.randint(1, 5)
      print(RED + "No es la Respuesta correcta", nombre, "!"+ RESET)
  
  print(YELLOW + "\nHola", nombre, "vas obteniendo", puntaje,"puntos en mi trivia" + RESET)
    

  time.sleep(2)  # Espera 1 segundo antes de continuar.
  print(CYAN + "\nPregunta 2\n")
  
  print("\n2) ¿Cuál es el animal nacional de Perú?\n")
  
  print("a) Gallito de las Rocas")
  print("b) Condor")
  print("c) Mono")
  print("d) Cocodrillo" + RESET)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input(GREEN + "\nTu respuesta: "+RESET)
  time.sleep(1)  # Espera 1 segundo antes de continuar.
  while respuesta_2 not in (GREEN +"a", "b", "c", "d", "x"+RESET):
    respuesta_2 = input(GREEN +"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: " +RESET)
    # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
    if respuesta_2 == "b":
      puntaje -= random.randint(1, 5)
      print(RED + "Incorrecto!", nombre,"El cóndor andino habita a lo largo de la Cordillera de los Andes y anida en acantilados rocosos."+RESET)  
    elif respuesta_2 == "c":
      puntaje -= random.randint(1, 5)
      print( RED + "Incorrecto!", nombre,"El Mono es un animal mamifero que lo encontramos con mayor frecuencia en las zonas calidas y selvaticas."+RESET)
    elif respuesta_2 == "d":
      puntaje -= random.randint(1, 5)
      print(RED + "Incorrecto!", nombre,"El Cocodrilo son grandes reptiles semiacuaticos que viven en zonas tropicales."+ RESET)
    elif respuesta_2 == "x":
      puntaje += 50
      print(GREEN +"Dato curioso: El gallito de las Rocas son grandes diseminadores de semillas en la Selva, lo que contribuye a la preservación de los bosques."+ RESET)
    else:
      puntaje += random.randint(5, 15)
      print(GREEN +"Muy bien", nombre, "!"+ RESET)
      
  
  print(YELLOW + "\nHola", nombre, "vas obteniendo", puntaje,"puntos en mi trivia" + RESET)

  time.sleep(2)  # Espera 1 segundo antes de continuar.
  print(CYAN + "\nPregunta 3\n")
  
  print("\n3) ¿En qué año llegó Cristóbal Colón al continente Americano?\n")
  
  print("a) 1300")
  print("b) 1492")
  print("c) 1498")
  print("d) 1500" + RESET)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_"
  respuesta_3 = input(GREEN + "\nTu respuesta: ")
  
  time.sleep(1)  # Espera 1 segundo antes de continuar.
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: " +RESET)
  
    if respuesta_3 == "a":
      print(RED + "Totalmente incorrecto! ..." + RESET)
      puntaje = puntaje / 2
    elif respuesta_3 == "c":
      print(RED + "Medianamente incorrecto" + RESET)
      puntaje = puntaje + 5
    elif respuesta_3 == "d":
      print(RED + "Incorrecto! ..." + RESET)
      puntaje = puntaje - 5
    else:
      print(GREEN + "Muy bien", nombre, "!" + RESET)
      puntaje = puntaje * 2
      
    time.sleep(1)  # Espera 1 segundo antes de continuar.
    print(YELLOW + "\nHola", nombre, "vas obteniendo", puntaje,"puntos en mi trivia" + RESET)
  
  time.sleep(2)  # Espera 1 segundo antes de continuar.
  print(CYAN + "\nExtra\n")
  
  numero_usuario = int(input("Escriba un numero de 0 a 4:\n" + RESET))
  if numero_usuario == 0:
      puntaje = puntaje / 2
  
  elif numero_usuario == 1:
      puntaje = puntaje + 5
  
  elif numero_usuario == 3:
      puntaje = puntaje - 5
  
  else:
      numero_usuario == 4
      puntaje = puntaje * 2
  
  time.sleep(1)  # Espera 1 segundo antes de continuar.
  print(YELLOW + "\nGracias", nombre, "por jugar mi trivia, alcanzaste", puntaje,"puntos" +RESET)
  
  time.sleep(2)  # Espera 1 segundo antes de continuar.
  print(CYAN + "\nPrueba tu Suerte\n")
  
  num1 = int(input("Ingrese tu dia de Nacimiento:"))
  num2 = int(input("Ingrese tu edad:" + RESET))
  op = input(CYAN + "Ingrese la operacion:" + RESET)
  num3 = num1 + num2 + puntaje
  time.sleep(1)  # Espera 1 segundo antes de continuar.

  for numero_carga in range(5, 0, -1):
     print(numero_carga, "...")
  time.sleep(1)
  while respuesta_3 not in ("+", "-", "/", "*"):
    respuesta_3 = input("Debes responder +, -, * o /. Ingresa nuevamente tu respuesta: " +RESET)
    
    if op == "+":
      print(YELLOW +"Excelente, has obtenido" , num1 + num2 + puntaje, "puntos"+ RESET)
    elif op == "-":
      print(YELLOW +"Excelente, has obtenido" , num1 - num2 + puntaje, "puntos"+ RESET)
    elif op == "*":
      print(YELLOW +"Excelente, has obtenido" , num1 * num2 + puntaje, "puntos"+ RESET)
    elif op == "/":
      print(YELLOW +"Excelente, has obtenido:" , num1 / num2 + puntaje, "puntos"+ RESET)
    else:
      print(RED + "operador invalido ." + RESET)
  
  
  print(BLUE +"\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+ RESET).lower()

  if repetir_trivia != "si":  # != significa "distinto"
    print(YELLOW +"\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!"+ RESET)
  iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.