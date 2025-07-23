def check_numbers(func):
    def wrapper(*args):
        for arg in args:
            try:
                float(arg)
            except ValueError:
                print(f'{arg} is not a number')
                return None
        return func(*args)
    return wrapper

@check_numbers
def addition(*args):
    sum_total = 0
    for index, arg in enumerate(args):
        sum_total+=arg
    return sum_total


@check_numbers
def multiplication(*args):
    sum_total = 1
    for index, arg in enumerate(args):
        temp=arg
        sum_total = temp*sum_total
    return sum_total


print(f'Result of addition is {addition(1,2,3)}')
print(f'Result of multiplication is {multiplication(4,2,3)}')

print(f'Result of addition is {addition(1,2,'manrique')}')
print(f'Result of multiplication is {multiplication(4,'maria',3)}')