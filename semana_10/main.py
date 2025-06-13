import utilities.menu as menu
import utilities.other as other
option=0
students=[]

if __name__ == "__main__":
    while True:
        try:    
            option = menu.select_option() 
            if option == 1:
                other.add_student(students)
            elif option == 2:
                other.show_students_records(students)
            elif option == 3:
                other.show_top3(students)
            elif option == 4:
                other.calculate_average_grade(students)
            elif option == 5:
                other.export_to_file("Students List.csv",students)
            elif option == 6:
                students = []
                other.import_from_file("Students List.csv",students)    
            elif option == 7:
                break
            else:
                print ("***Invalid Entry***")
                print ("Please enter a number (1 - 7)")
        except ValueError as error:
            print ("***Invalid Entry***")
            print("Please enter a number (1 - 7)")