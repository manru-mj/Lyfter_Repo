import csv
data_list=["Full name", "Last name","First name","Class", "Spanish grade","English grade", "History grade","Science grade", "Average grade"]
keys_list=["full_name", "last_name","first_name","class", "spanish_grade","english_grade", "history_grade","science_grade","average"]

def add_student(student_list):
    while True:
        flag = True
        temp_student={}
        temp_average=0
        for i in range(1, len(data_list)-1):
            if i<4 :
                temp_student[keys_list[i]] = input(f"Enter the {data_list[i]}: ")
            else:
                while True:
                    try:
                        temp_student[keys_list[i]] = int(input(f"Enter the {data_list[i]}: "))
                        if 0 <= temp_student[keys_list[i]] <=100:
                            temp_average += temp_student[keys_list[i]]
                            break
                        else:
                            print("Invalid Entry, type a value (0-100)")
                    except ValueError as error:
                        print("Invalid Entry, type a value (0-100)")
        temp_student["full_name"] = f"{temp_student["last_name"]} {temp_student["first_name"]}"
        temp_student["full_name"] = temp_student["full_name"].title()
        temp_student["average"] = str(temp_average/4)
        student_list.append(temp_student)
        while flag:
            option = str(input("Add another student?(Y/N): "))    
            if not (option == "N" or option == "n" or option == "Y" or option == "y"):
                print("Invalid Entry")
            else:
                flag = False
        if option == "N" or option == "n":
            break
    return temp_student


def show_students_records(student_list):
    if not student_list:
        print("""No records have been added yet!
            """)
    else:
        student_list.sort(key=lambda k:k["full_name"])
        print("Students Report")
        print()
        for i in range(0, len(student_list)):
            for j in range(0, len(data_list)):
                if j == 1 or j == 2:
                    continue
                print(f"{data_list[j]}: {student_list[i][keys_list[j]]}")
            print()


def show_top3(student_list):
    if not student_list:
            print("""No records have been added yet!
                """)
    else:
        try:
            for std in student_list:
                std["average"] = float(std["average"])
            
            student_list.sort(key=lambda k:k["average"],reverse=True)
            print("Student's Top 3")
            for i in range(0, 3):
                print()
                for j in range(0, len(data_list)):
                    if 0<j< len(data_list)-1:
                        continue
                    print(f"{data_list[j]}: {student_list[i][keys_list[j]]}")
            print()
        except IndexError:
            print("End of the list")
            print()


def calculate_average_grade(student_list):
    overall_average=0
    temp=0
    count=0
    if not student_list:
        print("""No records have been added yet!
            """)
    else:
        for i in student_list:
            temp += float(i["average"])
            count+=1
        overall_average= temp/count
        overall_average = round(overall_average,2)
        print(f"The overall average grade is {overall_average}")
        print()


def export_to_file(file_path,student_list):
    if not student_list:
        print("""No records have been added yet!
            """)
    else:
        with open(file_path,'w',encoding = 'utf-8') as file:
            writer = csv.DictWriter(file, keys_list)
            writer.writeheader()
            writer.writerows(student_list)
        print("The file Students List.csv has been saved")
        print()


def import_from_file(file_path,t_list):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            t_list.append(row)
    print("Data has been imported from file Students List.csv")
    print()