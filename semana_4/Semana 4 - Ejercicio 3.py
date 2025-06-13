import random

secret_number = int(random.randint (1,10))
num = int(input("Ingrese un número del 1 al 10: "))


while (num != secret_number):
    if(num != secret_number):
        num = int(input("Intente de nuevo: "))
    else:
        break        

print("Acertó! Fin del juego.")