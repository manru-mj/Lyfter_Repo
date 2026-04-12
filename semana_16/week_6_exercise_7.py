def is_prime(parameter):
    if parameter == 2:
        return True
    elif parameter <= 1:
        return False

    for i in range(2,parameter):
        if parameter % i == 0:
            return False
    
    return True

def create_prime_list(parameter):
    prime_list = []
    for i in range(0,len(parameter)):
        if is_prime(parameter[i]):
            prime_list.append(parameter[i])
    return prime_list


# main_list = [3,1,25,23,11,17,18,33,65,72,91]
main_list = [1,2,3,4,5,6,7,8,9]
# main_list = []
print(main_list)
print(create_prime_list(main_list))