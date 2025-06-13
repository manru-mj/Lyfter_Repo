def print_file(path):
    i = 1
    with open(path) as file:
        for line in file.readlines():
            print(f"Line {i}: {line}")
            i += 1


def file_to_list(path, parameter):
    with open(path) as file:
        for line in file.readlines():
            parameter.append(line)
        parameter.sort()
    return parameter

def list_to_sorted_file(path1,parameter1):
    with open(path1,"w") as file:
        for song in parameter1:
            file.write(song)

songs_list=[]

print("List before sorting:")
print_file("Songs.txt")
list_to_sorted_file("Sorted Songs.txt", file_to_list("Songs.txt", songs_list))
print("Sorted List:")
print_file("Sorted Songs.txt")