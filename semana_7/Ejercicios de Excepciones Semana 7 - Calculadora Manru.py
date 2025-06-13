def display_menu (number):
    menu_list = [
    "Addition", 
    "Subtraction", 
    "Multiplication", 
    "Division", 
    "Clear result",
    "Exit" 
    ]
    for i in range (0,len(menu_list)):
        print(f"{i+1}. {menu_list[i]}") 
    print(f"""Current result: {number}
        """)

def addition (number1, number2):
    number1 += number2
    return number1

def subtraction (number1, number2):
    number1 = number1-number2
    return number1 


def multiplication (number1, number2):
    number1 = number1*number2
    return number1 


def division (number1, number2):
    try:
        number1 = number1/number2
        return number1 
    except ZeroDivisionError as error:
        print(f"Error: {error}")
        return 0 


def clear_result (number1):
    number1 = 0
    return number1 

def execute_calculator():
    starting_number = 0
    new_number=0
    
    while True: 
        display_menu(starting_number)
        option = int(input("Select an option: "))
        
        if option == 1:
            new_number = int(input("Type a number: "))
            starting_number = addition(starting_number,new_number)
            
        if option == 2:
            new_number = int(input("Type a number: "))
            starting_number = subtraction(starting_number,new_number)
            
        if option == 3:
            new_number = int(input("Type a number: "))
            starting_number = multiplication(starting_number,new_number)
            
        if option == 4:
            new_number = int(input("Type a number: "))
            starting_number = division(starting_number,new_number)
            
        if option == 5:
            starting_number = clear_result(starting_number)
            
        if option == 6:
            break
        if option < 1 or option > 6:
            print("invalid option")
    

try:
    execute_calculator()
except ValueError as error:
    print(f"There was an error: {error}")
    


