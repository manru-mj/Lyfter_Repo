list_length = int(input("Enter the lenght of your list: "))
my_list = []
count = 0

for i in range (0, list_length):
    num = int(input(f"Enter number [ {i} ]: "))
    my_list.append(num)

print(my_list)

#for i in range (0, list_length):
while count < list_length :
    if my_list[count] % 2 == 0 :
        count += 1
    else:
        my_list.pop(count)
        list_length -= 1 
        if count > 0 :
            count -= 1
        else:
            count = 0


print(my_list)