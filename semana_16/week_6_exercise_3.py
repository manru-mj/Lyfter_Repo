numbers_list = []
numbers_list2 = [24,79,55,17]
numbers_list3 = [150,800,65,71,7,215,890,1215,24,79,55,17]

def sum_numbers_list(parameter):
    temp = 0
    if not isinstance(parameter, list):
        raise TypeError("Input must be a list")
    
    for element in parameter:
        if not isinstance(element, (int, float)):
            raise TypeError("All elements must be numbers")
        temp += element
    return temp


print(sum_numbers_list(numbers_list2))
#print(sum_numbers_list(numbers_list2))
#print(sum_numbers_list(numbers_list3))