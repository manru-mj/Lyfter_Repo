cantidad_notas = 0
contador = 1
notas_aprobadas = 0
notas_reprobadas = 0
promedio_total = 0
promedio_aprobadas = 0
promedio_reprobadas = 0
nota = 0


cantidad_notas = int(input("Ingrese la cantidad de notas: "))

while(contador<=cantidad_notas):
    nota = int(input(f"Ingrese la nota número {contador}: "))
    contador = contador + 1
    if(nota>70):
        notas_aprobadas = notas_aprobadas + 1
        promedio_aprobadas = promedio_aprobadas + nota
        promedio_total = promedio_total + nota
    else:
        notas_reprobadas = notas_reprobadas + 1
        promedio_reprobadas = promedio_reprobadas + nota
        promedio_total = promedio_total + nota

print(f"La cantidad de notas aprobadas es: {notas_aprobadas}")
print(f"La cantidad de notas reprobadas es: {notas_reprobadas}")
print(f"La nota promedio es: {promedio_total / cantidad_notas}")
print(f"El promedio de notas aprobadas es: {promedio_aprobadas / notas_aprobadas}")
print(f"El promedio de notas reprobadas es: {promedio_reprobadas / notas_reprobadas}")