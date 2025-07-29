def check_numbers(func):
    def wrapper(*args, **kwargs):
        # Validar args
        for arg in args:
            try:
                float(arg)
            except ValueError:
                raise ValueError(f'{arg} is not a number')

        # Validar kwargs
        for key, value in kwargs.items():
            try:
                float(value)
            except: 
                raise ValueError (f'{key}={value} is not a number')
        return func(*args, **kwargs)
    return wrapper

@check_numbers
def addition(*args,**kwargs):
    sum_total = sum(args)+sum(kwargs.values())
    return sum_total


@check_numbers
def multiplication(*args,**kwargs):
    product = 1
    for i in args:
        product *= i
    for x in kwargs.values():
        product *= x
    return product


try:
    print(f'Result of addition is {addition(1,2,3,other_num1=5, other_num2=6)}')
except ValueError as e:
    print(f"Error: {e}")

try:
    print(f'Result of multiplication is {multiplication(4,2,3,5)}')
except ValueError as e:
    print(f"Error: {e}")

try:
    print(f'Result of addition is {addition(1,2,'manrique')}')
except ValueError as e:
    print(f"Error: {e}")

try:
    print(f'Result of multiplication is {multiplication(4,'maria',3)}')
except ValueError as e:
    print(f"Error: {e}")