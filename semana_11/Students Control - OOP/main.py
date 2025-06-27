from menu import Menu
from student_manager import Student_Manager

menu_tile = "\nSelect an option:"
menu_options = ["1. Add new Student",
        "2. Students report",
        "3. Student's Top 3",
        "4. Average grade",
        "5. Export to file",
        "6. Import from File",
        "7. Exit"]
students_list =[]

if __name__ == "__main__":
    new_menu = Menu(menu_tile,menu_options,len(menu_options))
    new_student_manager = Student_Manager(students_list)
    is_running = True
    
    while is_running:
        option = new_menu.select_option()        
        
        if option == 1:
            keep_going = True
            new_student_manager.add_student()
            
            while keep_going:
                add_another = str(input("Add another student?(Y/N): "))    
                if add_another.lower() == "y":
                    new_student_manager.add_student()

                elif add_another.lower() == "n":
                    keep_going = False

                else:
                    print("Invalid Entry. Please enter Y or N")

        elif option == 2:
            new_student_manager.show_students_records()

        elif option == 3:
            new_student_manager.show_top3()

        elif option == 4:
            new_student_manager.calculate_average_grade()

        elif option == 5:
            new_student_manager.export_to_file("Students List.csv")

        elif option == 6:
            new_student_manager.import_from_file("Students List.csv")    

        elif option == 7:
            print("You have selected to exit. Goodbye!")
            is_running = False

