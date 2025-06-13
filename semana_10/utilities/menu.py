def print_menu():
    print("""Select an option:
        1. Add new Student
        2. Students report
        3. Student's Top 3
        4. Average grade
        5. Export to file
        6. Import from File
        7. Exit""")


def select_option():
    print_menu()
    option = int(input("Type your option: "))
    print()
    return option