numbers_list = [2,15,23,78,54,16]
numbers_list2 = [24,79,55,17]
numbers_list3 = [150,800,65,71,7,215,890,1215,24,79,55,17]

def sum_numbers_list(parameter):
    temp = 0
    for i in range(0, len(parameter)):
        temp += parameter[i]
    return temp


print(sum_numbers_list(numbers_list))
print(sum_numbers_list(numbers_list2))
print(sum_numbers_list(numbers_list3))