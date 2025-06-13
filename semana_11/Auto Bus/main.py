from Bus import AutoBus
from Persons import Person 

if __name__ == "__main__": 
    new_bus = AutoBus(int(input("Enter the maximum number of passengers: ")))
    counter = 0
    running = True

    while running == True:
        print("1. Board a passenger")
        print("2. Offboard a passenger")
        print("3. Exit")
        option = int(input("Select an option: "))
        if option == 3:
            running = False
        elif option == 1:
            new_passenger = Person()
            new_bus.board_passenger(new_passenger)
        elif option == 2:
            new_bus.offboard_passenger()