def invert_string(parameter):
    new_string = ""
    if not isinstance(parameter, str):
        raise TypeError("Input must be a String")
    
    for i in range(len(parameter),0,-1):
        new_string += parameter[i-1]
    return new_string    


# my_string = input("Type a String: ")
# print(f"The inverted string is: {invert_string(my_string)}")