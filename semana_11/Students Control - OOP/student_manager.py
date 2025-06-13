import csv
from typing import Self
from students import Student

class Student_Manager():
    
    def __init__(self,student_list):
        self.student_list = student_list
        self.data_list=["Last name","First name","Class", "Spanish grade","English grade", "History grade","Science grade", "Average grade"]
        self.keys_list=["last_name","first_name","class", "spanish_grade","english_grade", "history_grade","science_grade","average"]


    def get_valid_value(self,subject):
        running = True
        while running:
            try:
                grade = int(input(f"Enter the {subject} grade (0-100): "))
                if 0 <= grade <= 100:
                    return grade
                else:
                    print("Invalid Entry, type a value (0-100)") 
            except ValueError as error:
                        print("Invalid Entry, type a value (0-100)")


    def create_student(self):
        last_name = input("Enter the Last name: ")
        first_name = input("Enter the First name: ")
        class_id = input("Enter the Class: ")
        spanish_grade = self.get_valid_value("Spanish")
        english_grade = self.get_valid_value("English")
        history_grade = self.get_valid_value("History")
        science_grade = self.get_valid_value("Science")
        average = (spanish_grade+english_grade+history_grade+science_grade)/4
        new_student = Student(last_name,first_name,class_id,spanish_grade,english_grade,history_grade,science_grade,average)
        return new_student


    def convert_student_to_dictionary(self,param_student):    
        student_dict = {}
        student_dict["last_name"] = param_student.last_name
        student_dict["first_name"] = param_student.first_name
        student_dict["class"] = param_student.class_id
        student_dict["spanish_grade"] = param_student.spanish_grade
        student_dict["english_grade"] = param_student.english_grade
        student_dict["history_grade"] = param_student.history_grade
        student_dict["science_grade"] = param_student.science_grade
        student_dict["average"] = param_student.average
        return student_dict


    def add_student(self):
        new_student = self.create_student()
        self.student_list.append(self.convert_student_to_dictionary(new_student))

    
    def show_students_records(self):
        if not self.student_list:
            print("""No records have been added yet!
                """)
        else:
            self.student_list.sort(key=lambda k:k["last_name"])
            print("Students Report\n")
            for i in range(0, len(self.student_list)):
                for j in range(0, len(self.data_list)):
                    print(f"{self.data_list[j]}: {self.student_list[i][self.keys_list[j]]}")
                print()


    def show_top3(self):
        if not self.student_list:
                print("""No records have been added yet!
                    """)
        else:
            try:
                for student in self.student_list:
                    student["average"] = float(student["average"])
                
                self.student_list.sort(key=lambda k:k["average"],reverse=True)
                print("\nStudent's Top 3")
                for i in range(0, 3):
                    print(f"\nFull Name: {self.student_list[i]["last_name"]} {self.student_list[i]["first_name"]}")
                    print(f"Average grade: {self.student_list[i]["average"]}")
            except IndexError:
                print("End of the list\n")
    

    def calculate_average_grade(self):
        overall_average=0
        temp=0
        count=0
        if not self.student_list:
            print("""No records have been added yet!
                """)
        else:
            for i in self.student_list:
                temp += float(i["average"])
                count+=1
            overall_average= temp/count
            overall_average = round(overall_average,2)
            print(f"\nThe overall average grade is {overall_average}")


    def export_to_file(self,file_path):
        if not self.student_list:
            print("No records have been added yet!\n")
        else:
            with open(file_path,'w',encoding = 'utf-8') as file:
                writer = csv.DictWriter(file, self.keys_list)
                writer.writeheader()
                writer.writerows(self.student_list)
            print("The file Students List.csv has been saved\n")
    

    def import_from_file(self,file_path):
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.student_list.append(row)
            print("Data has been imported from file Students List.csv\n")
        except Exception as error:
            print ("Unable to export yet.")