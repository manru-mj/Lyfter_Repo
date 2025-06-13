var_test = "Exercise 2 - First part, trying to access a private variable"
        

def function_test1 ():
    var_test1 = "Private variable"


def change_var_test():
    parameter = "This is the value of the global variable after being changed by the function"
    return parameter

print(var_test)
#print(var_test1) Can't Access it

var_test = change_var_test()

print(var_test)