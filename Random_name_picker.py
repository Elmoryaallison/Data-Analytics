print("Name pairing program.\n")
import random

names_list = ["Allison", "Clifford", "Anton", "El Morya", "Bliss", "Darla"]
lists = [1, 2, 3]

for item in lists:
    enter_name = input("Hello! Please enter your name: ")

    try:

        if enter_name == "Allison" or enter_name == "Clifford" or enter_name == "Anton" or enter_name == "El Morya" or enter_name == "Bliss" or enter_name == "Darla":
            names_list.remove(enter_name)
            name = random.choice(names_list)
            

    except ValueError:   
        print("Name not found. Try another name:\n")
        enter_name = input(f'Available names {names_list}: ')
        names_list.remove(enter_name)
        name = random.choice(names_list)

        

    print(f'{enter_name} is to gift {name} a present!')
    names_list.remove(name)
    print(f'Available names: {names_list}')

else:
    print("Name pairing complete!")
    
