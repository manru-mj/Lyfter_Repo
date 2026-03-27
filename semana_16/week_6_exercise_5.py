def count_upper_lower(parameter):
    lower_count = 0
    upper_count = 0
    if not isinstance(parameter, str):
        raise TypeError("Input must be a string")
    
    for i in range(0,len(parameter)):
        if str.isalpha(parameter[i]):    
            if str.islower(parameter[i]):
                lower_count += 1
            else:
                upper_count += 1
    return upper_count, lower_count 


# my_string = input("Type a String: ")
# upper, lower = count_upper_lower(my_string)
# print(f"There're {upper} upper cases and {lower} lower cases")