import csv

def write_file(path,data, header):
    with open(path,'a',encoding = 'utf-8') as file:
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(data)


def create_temp_list(list_1,list_2):
    while True:
        temp = {}
        for i in range(0,len(list_1)):
            temp[list_1[i]] = input(f"Enter the {list_1[i]}: ")
        list_2.append(temp)        
        option = input("Add another game (Y/N): ")
        if option == "N" or option == "n":
            break 


game_list_headers = [
    'Name',
    'Genre',
    'Developer',
    'ESRB Rating'
]

temp_list=[]

create_temp_list(game_list_headers,temp_list)
write_file("Games.csv",temp_list, game_list_headers)