def convert_string_to_list(parameter):
    count = 0
    my_list = [""]
    for i in range(0,len(parameter)):
        if parameter[i] == '-' :
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

def process_string(parameter):
    lista = convert_string_to_list(parameter)
    return convert_list_to_string(lista)

# my_string = input("Type random words separated by '-': ")
# print(process_string(my_string))