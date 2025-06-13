import json

def show_pokedex(path):
    with open(path,"r",encoding="utf-8") as file:
        data = json.load(file)
    for i in range(0,len(data)):
        temp = data[i]
        name = data[i]['name']['english']
        poke_type = data[i]['type']
        poke_hp = data[i]['base']['HP']
        poke_attack = data[i]['base']['Attack']
        poke_defense = data[i]['base']['Defense']
        poke_sp_attack = data[i]['base']['Sp. Attack']
        poke_sp_defense = data[i]['base']['Sp. Defense']
        poke_speed = data[i]['base']['Speed']
        print(f"{i+1}. Name: {name}")
        for count in range(0,len(poke_type)):
            print(f"Type {count+1}: {poke_type[count]}")
        print(f"HP: {poke_hp}")
        print(f"Attack: {poke_attack}")
        print(f"Defense {poke_defense}")
        print(f"Sp. Attack:{poke_sp_attack}")
        print(f"Sp. Defense: {poke_sp_defense}")
        print(f"Speed: {poke_speed}")


def enter_new_pokemon():
    poke_type = []
    poke_base_values = []
    poke_base_keys = ["HP","Attack","Defense","Sp. Attack","Sp. Defense","Speed"]
    new_pokemon = {}
    temp={}

    poke_name = str(input("Enter new pokemon's name: "))
    option = str(input("Is this pokemon multi-type (Y/N): "))
    if option == "N" or option == "n":
        poke_type.append(str(input("Enter new pokemon's type: ")))
    else:
        for i in range(0,2):
            poke_type.append(str(input(f"Enter new pokemon's type {i+1}: ")))

    for i in range(0,len(poke_base_keys)):
        poke_base_values.append(int(input(f"Enter new pokemon's {poke_base_keys[i]}: ")))

    new_pokemon["name"] = {"english":poke_name}
    new_pokemon["type"] = poke_type
    for i in range(0, len(poke_base_keys)):
        temp[poke_base_keys[i]] = poke_base_values[i]
    new_pokemon["base"] = temp

    return new_pokemon


def add_new_pokemon(path,new_pm):
    with open(path,"r",encoding="utf-8") as dex:
        data = json.load(dex)

    data.append(new_pm)

    with open(path,"w",encoding="utf-8") as dex:
        json.dump(data,dex,indent=4,ensure_ascii=False)


show_pokedex("Pokemon List.json")
new_item = enter_new_pokemon()
add_new_pokemon("Pokemon List.json",new_item)
show_pokedex("Pokemon List.json")