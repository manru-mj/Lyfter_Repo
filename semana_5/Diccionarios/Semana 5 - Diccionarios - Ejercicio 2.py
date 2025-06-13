list_a = ["first_name", "last_name", "city", "age"]
list_b = ["Manrique","Corrales","Alajuela",42]

my_dictionary = {}

for i in range(0, len(list_a)):
    my_dictionary[list_a[i]] = list_b[i]

print(my_dictionary)
    