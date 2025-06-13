first = 0
last = 0
my_list = []


temp_list = input("Write a string to be convented in a list of characters: ")
last = len(temp_list)-1

for i in range(0, len(temp_list)):
    my_list.append(temp_list[i])

temp = my_list[last]
my_list[last] = my_list[first]
my_list[first] = temp

print(my_list)