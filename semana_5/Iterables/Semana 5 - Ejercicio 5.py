print("Please enter 10 numbers ")
my_list = []
temp = 0


for i in range(0,10):
    my_list.append (int(input(f"Enter number {i+1}: ")))
    if my_list[i] > temp:
        temp=my_list[i]

print(my_list)
print(f"The greatest number was {temp}" )