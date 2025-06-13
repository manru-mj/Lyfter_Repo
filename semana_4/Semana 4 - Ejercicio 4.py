num_mayor = 0
num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercer número: "))

num_mayor = num_1

if(num_2>num_mayor):
    num_mayor = num_2
elif(num_3>num_mayor):
    num_mayor = num_3

print(f"El número mayores: {num_mayor}")
