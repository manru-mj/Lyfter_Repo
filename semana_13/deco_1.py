def print_params_and_return(func):
    def wrapper(*args):
        print(f'Function: {func.__name__}')
        print(f'Parameters: {args}')
        result = func(*args)
        print(f'{func.__name__} returned {result}')
    return wrapper


@print_params_and_return
def addition(*args):
    sum_total = 0
    for index, arg in enumerate(args):
        sum_total+=arg
    return sum_total


@print_params_and_return
def multiplication(*args):
    sum_total = 1
    for index, arg in enumerate(args):
        temp=arg
        sum_total = temp*sum_total
    return sum_total


addition(1,2,3)
multiplication(4,2,3)


