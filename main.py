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
print("\033[35m"+cadena.center(80, " "))
for numero_carga in range(3, 0, -1):
    print(numero_carga, "...")
    time.sleep(1)
print("\n")
print("Pondremos a Prueba tus Conocimientos:\n\033[39m")
time.sleep(1)
# Agregaremos personalizacion a nuestros jugadores, preguntando y almacenando sus nombres en una variable.
nombre = input("\033[34mIngresa tu Nombre:\033[39m")
time.sleep(0.5)
apellido = input("\033[34mIngresa tus Apellidos:\033[39m")
time.sleep(0.5)
edad = input("\033[34mIngresa tu Edad:\033[39m")
time.sleep(1)

print("\033[36m\nHola", nombre, apellido,
      "Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
time.sleep(1)

for numero_carga in range(3, 0, -1):
    print(numero_carga, "...")
    time.sleep(1)
print("\n\033[39m")
while iniciar_trivia == True:
    intentos += 1
    puntaje += puntaje
    print("Intento número:", intentos)
    input("Presiona Enter para continuar")
    print("\033[33m comenzaras con :", puntaje, "puntos\n\033[39m")
    time.sleep(1)
    # Aqui van las preuntas
    print("\033[36mPregunta 1\n")
    print("1) ¿Cuál fue la serie más vista en Netflix en el 2019?\n\033[39m")
    # Colocamos las alternativas
    alternativas_1 = ["a) Locke and Key", "b) Stranger Things",
                      "c) Betty la Fea", "d) Better Call Saul"]
    for number in range(0, 4):
        print("\033[36m", alternativas_1[number], "\033[39m")
    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta_1 = input("\nTu respuesta: ")
    time.sleep(1)
    while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input(
            "\033[35m Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: \033[39m")
    if respuesta_1 == "b":
        puntaje += random.randint(0, 50)
        print("\033[32m\nMuy bien", nombre, "! Sigue asi!\033[39m")
    else:
        puntaje -= random.randint(0, 60)
        print("\033[31m\nNo es la Respuesta correcta", nombre, "!"+"\033[39m")

    print("\033[33m\nHola", nombre, "vas obteniendo",
          puntaje, "puntos en mi trivia" + "\033[39m")

    time.sleep(2)
    print("\033[36m\nPregunta 2\n")
    print("\n2) ¿Cuál es el animal nacional de Perú?\n\033[39m")
    alternativas_2 = ["a) Gallito de las Rocas", "b) Condor",
                      "c) Mono", "d) Cocodrillo"]
    for number in range(0, 4):
        print("\033[36m",alternativas_2[number], "\033[39m")
    # Almacenamos la respuesta del usuario en la variable "respuesta_2"
    respuesta_2 = input("\nTu respuesta: ")
    time.sleep(1)
    while respuesta_2 not in ("a", "b", "c", "d", "x"):
        respuesta_2 = input(
            "\033[35mDebes responder a, b, c o d. Ingresa nuevamente tu respuesta: \033[39m")
    # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
    if respuesta_2 == "b":
        puntaje -= random.randint(0, 40)
        print("\033[31m\nIncorrecto!\033[39m" "\033[32m", nombre,
              "El cóndor andino habita a lo largo de la Cordillera de los Andes y anida en acantilados rocosos.\033[39m")
    elif respuesta_2 == "c":
        puntaje -= random.randint(0, 40)
        print(RED + "\nIncorrecto!", nombre,
              "El Mono es un animal mamifero que lo encontramos con mayor frecuencia en las zonas calidas y selvaticas."+RESET)
    elif respuesta_2 == "d":
        puntaje -= random.randint(0, 40)
        print(RED + "\nIncorrecto!", nombre,
              "El Cocodrilo son grandes reptiles semiacuaticos que viven en zonas tropicales." + RESET)

    elif respuesta_2 == "x":
        puntaje += 100
        print(GREEN + "Dato curioso: El gallito de las Rocas son grandes diseminadores de semillas en la Selva, lo que contribuye a la preservación de los bosques.\033[39m")
    else:
        puntaje += random.randint(0, 60)
        print("\033[32m\nMuy bien", nombre, "!\033[39m")

    print(YELLOW + "\nHola", nombre, "vas obteniendo",
          puntaje, "puntos en mi trivia" + RESET)

    time.sleep(2)
    print(CYAN + "\nPregunta 3\n")
    print("\n3) ¿En qué año llegó Cristóbal Colón al continente Americano?\n")
    alternativas_3 = ["a) 1300", "b) 1492",
                      "c) 1498", "d) 1500"]
    for number in range(0, 4):
        print("\033[36m", alternativas_3[number], "\033[39m")
  # Almacenamos la respuesta del usuario en la variable "respuesta_"
    respuesta_3 = input("\nTu respuesta: ")
    time.sleep(1)
    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input(
            "\033[35mDebes responder a, b, c o d. Ingresa nuevamente tu respuesta: \033[39m")
    if respuesta_3 == "a":
        print(RED + "\nTotalmente incorrecto! ..." + RESET)
        puntaje = puntaje / 2
    elif respuesta_3 == "c":
        print(RED + "\nMedianamente incorrecto" + RESET)
        puntaje = puntaje + 25
    elif respuesta_3 == "d":
        print(RED + "\nIncorrecto! ..." + RESET)
        puntaje = puntaje - 35
    else:
        print(GREEN + "\nMuy bien", nombre, "!" + RESET)
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
        puntaje = puntaje + 25

    elif numero_usuario == 3:
        puntaje = puntaje - 35
    else:
        numero_usuario == 4
        puntaje = puntaje * 2

    time.sleep(1)
    print(YELLOW + "\nGracias", nombre,
          "por jugar mi trivia, alcanzaste", puntaje, "puntos" + RESET)

    time.sleep(2)
    print("\033[36m\nPrueba tu Suerte\n")
    num1 = int(input("Ingrese tu dia de Nacimiento:"))
    num2 = int(input("Ingrese tu edad:"))
    op = input("Ingrese la operacion:\033[39m")
    time.sleep(1)

    while op not in ("+", "-", "/", "*"):
        op = input(
            "\033[35mDebes responder +, -, * o /. Ingresa nuevamente tu respuesta: \033[39m")
    for numero_carga in range(5, 0, -1):
        print(numero_carga, "...")
        time.sleep(1)
    if op == "+":
        print("\033[\n32mExcelente, has obtenido",
              num1 + num2 + puntaje, "puntos\033[39m")
    elif op == "-":
        print("\033[32m\nExcelente, has obtenido",
              num1 - num2 + puntaje, "puntos\033[39m")
    elif op == "*":
        print("\033[32m\nExcelente, has obtenido",
              num1 * num2 + puntaje, "puntos\033[39m")
    elif op == "/":
        print("\033[32m\nExcelente, has obtenido:",
              num1 / num2 + puntaje, "puntos\033[39m")
    else:
        print("\033[31moperador invalido .\033[39m")

    # Aqui finalizamos o reiniciamos la trivia
    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
    # Aqui el jugador decide
    if repetir_trivia != "si":
        print("\033[32m\nEspero", nombre,
              "que lo hayas pasado bien, hasta pronto!\033[39m")
    # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
        iniciar_trivia = False