class Menu():
    def __init__(self,title,options,options_length):
        self.title = title
        self.options = options
        self.options_length = options_length


    def show_menu(self):# this method prints the list of options
        print(self.title)
        for option in self.options:
            print(option)


    def select_option(self):# this method calls show_menu, asks the user to enter an option and return the option's value
        self.show_menu()
        try:    
            option_selected = int(input("Select an option: "))
            if 0 < option_selected <= self.options_length:
                return option_selected
            else:
                print ("***Invalid Entry***")
                print("Please enter a number (1 - 7)")     
        except ValueError as error:
            print ("***Invalid Entry***")
            print("Please enter a number (1 - 7)")






#    print_menu()
#    option = int(input("Type your option: "))
#    print()
#    return option