def convert_string_to_list(parameter):
    count = 0
    my_list = [""]
    for i in range(0,len(parameter)):
        if my_string[i] == '-' :
            i += 1
            count += 1
            my_list.append("")
        else:
            my_list[count] = my_list[count] + str(parameter[i])
    return my_list


def convert_list_to_string(parameter):
    parameter.sort()
    my_str2 = ""
    for i in range(0,len(parameter)):
        if i == len(parameter)-1:
            my_str2 += parameter[i]
        else:
            my_str2 += parameter[i]
            my_str2 += "-"
    return my_str2

my_string = input("Type random words separated by '-': ")

print(my_string)
print(convert_list_to_string(convert_string_to_list(my_string)))
