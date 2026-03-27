def bubble_sort(num_list):
    swap_count = 0
    rounds_count = 0
    
    if not isinstance(num_list, list):
        raise TypeError("Input must be a list")
    
    for j in range(0, len(num_list)-1):
        for i in range(0, len(num_list)-1-j):
            temp = num_list[i]
            if num_list[i] > num_list[i+1]:
                swap_count += 1
                num_list[i] = num_list[i+1]
                num_list[i+1] = temp
            rounds_count += 1
    
    return num_list

def inverted_bubble_sort(num_list):
    swap_count = 0
    rounds_count = 0
    
    if not isinstance(num_list, list):
        raise TypeError("Input must be a list")
    
    for j in range(0, len(num_list)-1):
        for i in range(len(num_list)-1, j, -1):
            temp = num_list[i]
            if num_list[i] < num_list[i-1]:
                swap_count += 1
                num_list[i] = num_list[i-1]
                num_list[i-1] = temp
            rounds_count += 1
    
    return num_list

# my_list = [11,5,15,7,2,8,12,10,4,1,9,3,6,14,13]
# print(f"List to sort: {my_list}")
# print("Bubble Sort:")
# bubble_sort(my_list)

# my_list = [11,5,15,7,2,8,12,10,4,1,9,3,6,14,13]
# print(f"List to sort: {my_list}")
# print("Bubble Sort right to left:")
# inverted_bubble_sort(my_list)