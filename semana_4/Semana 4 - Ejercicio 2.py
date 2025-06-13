name = input("Ingrese el nombre: ")
last_name = input("Ingrese el apellido: ")
age = int(input("Ingrese la edad: "))

if ((age>0) and (age<=2)):
    print(f"{name} {last_name} es un Bebé.")
elif (age>2 and age<=9):
    print(f"{name} {last_name} es un Niño.")
elif (age>9 and age<=12):
    print(f"{name} {last_name} es un Preadolescente.")
elif (age>12 and age<=17):
    print(f"{name} {last_name} es un Adolescente.")
elif (age>17 and age<=29):
    print(f"{name} {last_name} es un Adulto joven.")
elif (age>29 and age<=59):
    print(f"{name} {last_name} es un Adulto.")
else:
    print(f"{name} {last_name} es un Adulto Mayor.")