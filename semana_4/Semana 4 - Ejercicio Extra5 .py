num=0
mayor=0
contador=1
while (contador<=5):
    num=int(input("Ingrese el numero "))
    contador=contador+1
    if(num>mayor):
        mayor=num


print("El numero mayor es: ",mayor)
