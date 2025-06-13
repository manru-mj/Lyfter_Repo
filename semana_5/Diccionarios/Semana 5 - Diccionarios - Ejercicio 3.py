list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

print(employee)

for i in range(0,len(list_of_keys)):
    employee.pop(list_of_keys[i])

print(employee)