def count_upper_lower(parameter):
    lower_count = 0
    upper_count = 0
    for i in range(0,len(parameter)):
        if str.isalpha(parameter[i]):    
            if str.islower(parameter[i]):
                lower_count += 1
            else:
                upper_count += 1
    print(f"There're {upper_count} upper cases and {lower_count} lower cases")


my_string = input("Type a String: ")
count_upper_lower(my_string)