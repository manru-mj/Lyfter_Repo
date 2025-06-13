from Persons import Person
class AutoBus():
    
    def __init__(self,max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []
        print(f"A new bus has been created with a maximum capacity of {self.max_passengers} passengers.")

    def board_passenger(self,passenger):
        if len(self.passengers) >= self.max_passengers:
            print("The bus is full, no more passengers allowed")
        else:
            print("A new passenger has boarded.")
            return self.passengers.append(passenger)


    def offboard_passenger(self):
        if len(self.passengers) == 0:
            print("The bus is empty.")
        else:
            print("A Passenger got off the bus.")
            return self.passengers.pop()