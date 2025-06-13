def is_prime(parameter):
    if parameter == 0:
        return False
    count = 0
    for i in range(2,parameter):
        if parameter%(i) == 0:
            count += 1  
    if count>0:
        return False
    else:
        return True


def create_prime_list(parameter):
    prime_list = []
    for i in range(0,len(parameter)):
        if is_prime(parameter[i]):
            prime_list.append(parameter[i])
    return prime_list


main_list = [3,1,25,23,11,17,18,33,65,72,91]
print(main_list)
print(create_prime_list(main_list))