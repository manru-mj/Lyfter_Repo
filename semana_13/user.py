from datetime import date, datetime


class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1  # aún no ha cumplido años este año
        return years
    
    
def adults_only(func):
    def wrapper(user, *args):
        if user.age < 18:
            print(f"{user.name} is not an adult (is {user.age} years old)")
        else:
            return func(user, *args,)
    return wrapper    

@adults_only
def admit_user(user):
    print(f"New user {user.name} has been admitted")



underage_user = User("Sergio", date(2023,11,30))
adult_user =  User("Manrique", date(1982,7,7))

admit_user(underage_user)
admit_user(adult_user)