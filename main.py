import time  # importamos la libreria tiempo
import random  # importamos la libreria random
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
puntaje = random.randint(0, 500)
iniciar_trivia = True
intentos = 0
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia.
cadena = "bienvenido a mi trivia sobre cultura general".title()
print(MAGENTA+cadena.center(100, " "))
for numero_carga in range(3, 0, -1):
    print(numero_carga, "...")
    time.sleep(1)
print("\n")
print("Pondremos a Prueba tus Conocimientos:\n")
time.sleep(1)
# Agregaremos personalizacion a nuestros jugadores, preguntando y almacenando sus nombres en una variable.
nombre = input("\033[34mIngresa tu Nombre:\033[39m")
time.sleep(0.5)
apellido = input("\033[34mIngresa tus Apellidos:\033[39m")
time.sleep(0.5)
edad = input("\033[34mIngresa tu Edad:\033[39m")
time.sleep(1)

print(WHITE+"\nHola", nombre, apellido,
      "Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)
time.sleep(1)

for numero_carga in range(3, 0, -1):
    print(numero_carga, "...")
    time.sleep(1)

while iniciar_trivia == True:
    intentos += 1
    puntaje += puntaje
    print("\nIntento número:", intentos)
    input("Presiona Enter para continuar")
    print(YELLOW + "comenzaras con :", puntaje, "puntos\n" + RESET)
    time.sleep(1)
    # Aqui van las preuntas
    print(CYAN + "Pregunta 1\n")
    print("1) ¿Cuál fue la serie más vista en Netflix en el 2019?\n")
    # Colocamos las alternativas
    print("a) Locke and Key")
    print("b) Stranger Things")
    print("c) Betty la Fea")
    print("d) Better Call Saul")
    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta_1 = input("\nTu respuesta: ")
    time.sleep(1)
    while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    if respuesta_1 == "b":
        puntaje += random.randint(5, 15)
        print("\nMuy bien", nombre, "! Sigue asi!")
    else:
        puntaje -= random.randint(1, 5)
        print("\nNo es la Respuesta correcta", nombre, "!")

    print(YELLOW + "\nHola", nombre, "vas obteniendo",
          puntaje, "puntos en mi trivia" + RESET)

    time.sleep(2)
    print(CYAN + "\nPregunta 2\n")
    print("\n2) ¿Cuál es el animal nacional de Perú?\n")
    print("a) Gallito de las Rocas")
    print("b) Condor")
    print("c) Mono")
    print("d) Cocodrillo" + RESET)
    # Almacenamos la respuesta del usuario en la variable "respuesta_2"
    respuesta_2 = input(GREEN + "\nTu respuesta: ")
    time.sleep(1)
    while respuesta_2 not in ("a", "b", "c", "d", "x"):
        respuesta_2 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: " + RESET)
    # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
    if respuesta_2 == "b":
        puntaje -= random.randint(1, 5)
        print(RED + "Incorrecto!", nombre,
              "El cóndor andino habita a lo largo de la Cordillera de los Andes y anida en acantilados rocosos."+RESET)
    elif respuesta_2 == "c":
        puntaje -= random.randint(1, 5)
        print(RED + "Incorrecto!", nombre,
              "El Mono es un animal mamifero que lo encontramos con mayor frecuencia en las zonas calidas y selvaticas."+RESET)
    elif respuesta_2 == "d":
        puntaje -= random.randint(1, 5)
        print(RED + "Incorrecto!", nombre,
              "El Cocodrilo son grandes reptiles semiacuaticos que viven en zonas tropicales." + RESET)

    elif respuesta_2 == "x":
        puntaje += 50
        print(GREEN + "Dato curioso: El gallito de las Rocas son grandes diseminadores de semillas en la Selva, lo que contribuye a la preservación de los bosques.")
    else:
        puntaje += random.randint(5, 15)
        print("Muy bien", nombre, "!" + RESET)

    print(YELLOW + "\nHola", nombre, "vas obteniendo",
          puntaje, "puntos en mi trivia" + RESET)

    time.sleep(2)
    print(CYAN + "\nPregunta 3\n")
    print("\n3) ¿En qué año llegó Cristóbal Colón al continente Americano?\n")
    print("a) 1300")
    print("b) 1492")
    print("c) 1498")
    print("d) 1500" + RESET)
  # Almacenamos la respuesta del usuario en la variable "respuesta_"
    respuesta_3 = input(GREEN + "\nTu respuesta: ")
    time.sleep(1)
    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: " + RESET)
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
    time.sleep(1)
    print(YELLOW + "\nHola", nombre, "vas obteniendo",
          puntaje, "puntos en mi trivia" + RESET)

    time.sleep(2)
    print(CYAN+"\nPregunta Extra\n")

    numero_usuario = int(input("Escriba un numero de 0 a 4:"+RESET))
    if numero_usuario == 0:
        puntaje = puntaje / 2

    elif numero_usuario == 1:
        puntaje = puntaje + 5

    elif numero_usuario == 3:
        puntaje = puntaje - 5
    else:
        numero_usuario == 4
        puntaje = puntaje * 2

    time.sleep(1)
    print(YELLOW + "\nGracias", nombre,
          "por jugar mi trivia, alcanzaste", puntaje, "puntos" + RESET)

    time.sleep(2)
    print("\nPrueba tu Suerte\n")
    num1 = int(input("Ingrese tu dia de Nacimiento:"))
    num2 = int(input("Ingrese tu edad:"))
    op = input("Ingrese la operacion:")
    time.sleep(1)

    while op not in ("+", "-", "/", "*"):
        op = input(
            "Debes responder +, -, * o /. Ingresa nuevamente tu respuesta: ")
    for numero_carga in range(5, 0, -1):
        print(numero_carga, "...")
        time.sleep(1)
    if op == "+":
        print("Excelente, has obtenido",
              num1 + num2 + puntaje, "puntos")
    elif op == "-":
        print("Excelente, has obtenido",
              num1 - num2 + puntaje, "puntos")
    elif op == "*":
        print("Excelente, has obtenido",
              num1 * num2 + puntaje, "puntos")
    elif op == "/":
        print("Excelente, has obtenido:",
              num1 / num2 + puntaje, "puntos")
    else:
        print(RED + "operador invalido ." + RESET)

    # Aqui finalizamos o reiniciamos la trivia
    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
    # Aqui el jugador decide
    if repetir_trivia != "si":
        print("\nEspero", nombre,
              "que lo hayas pasado bien, hasta pronto!")
    # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
        iniciar_trivia = False