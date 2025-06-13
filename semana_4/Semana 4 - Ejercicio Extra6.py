num=int(input("Ingrese un numero: "))

if((num % 3 == 0) and (num % 5 == 0)):
    print("FizzBuzz")
elif (num % 5 == 0):
    print("Buzz")
elif  (num % 3 == 0):
    print("Fizz")
else:
    print("No es divisible entre 3 ni 5")
