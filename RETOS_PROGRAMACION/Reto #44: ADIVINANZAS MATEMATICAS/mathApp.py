from decimal import getcontext, Decimal
from os import _exit
import threading, random

TIMER_SECONDS = 3

# Funciones binarias
def sum(a, b):
    print(f"{a} + {b}:")
    return a + b

def substract(a, b):
    print(f"{a} - {b}:")
    return a - b

def multiply(a, b):
    print(f"{a} * {b}:")
    return a * b

def division(a, b):
    print(f"{a} : {b}:")
    getcontext().prec = 2
    resultado_decimal = Decimal(a) / Decimal(b)
    return resultado_decimal


# Funcion para crear operaciones aleatorias
def random_operation(cifra_a, cifra_b):
    a = random.randint(10 ** (cifra_a - 1), (10 ** cifra_a) - 1)
    b = random.randint(10 ** (cifra_b - 1), (10 ** cifra_b) - 1)
    
    operations = [sum, substract, multiply, division]
    operation = random.choice(operations)
    result = operation(a, b)
    
    return result

def answer_question(cont, cifra1, cifra2):
    print("Tienes 3 segundos para responder:")
    timer = threading.Timer(TIMER_SECONDS, exit_program, args=(cont,))
    timer.start()
    
    result = random_operation(cifra1, cifra2)
    while True:
        answer = input()
        if answer != str(result):
            print("Respuesta incorrecta. Otro intento")
        else:       
            timer.cancel()
            break
    

def exit_program(cont):
    print("¡Tiempo agotado! Programa cortado\n")
    print("Tus numero de aciertos: ", cont)
    _exit(0)


if __name__ == "__main__":
    cont = 0
    cifra_a = 1
    cifra_b = 1

    # Función para cronometrar y cortar el programa si excede el tiempo límite        
    while True:
        # Aumentos del número de cifras
        if cont > 0:
            if cont % 5 == 0 and (cont // 5) % 2 != 0:
                cifra_a += 1
            if cont % 10 == 0:
                cifra_b += 1

        answer_question(cont, cifra_a, cifra_b)

        cont += 1
