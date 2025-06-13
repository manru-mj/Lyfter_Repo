tiempo_segundos = int(input("Ingrese el tiempo en segundos: "))
if(tiempo_segundos>600):
    print("El tiempo es MAYOR a 10 minutos.")
else:
    print(f"Faltan {600 - tiempo_segundos} segundos.")