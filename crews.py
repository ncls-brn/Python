import random

def principal_menu():
    crew = [
        {
            "first_name": "Bel",
            "last_name": "Riose",
            "gender": "M",
            "age": 48,
            "role": "Commandant"
        },
        {
            "first_name": "Gaal",
            "last_name": "Dornick",
            "gender": "F",
            "age": 34,
            "role": "Engineer"
        },
    ]

    action_count = 0  

    while True:
        print("\nMenu:")
        print("1. Add member")
        print("2. Delete member")
        print("3. Display crew")
        print("4. Check if the crew is ready")
        print("5. Crew report")
        print("6. Exit")
        
        choice = input("Please select an option 1 to 6: ")

        match choice:
            case "1":
                add_member(crew)
            case "2":
                remove_member(crew)
            case "3":
                display_crew(crew)
            case "4":
                check_crew(crew)
            case "5":
                crew_report(crew)
            case "6":
                print("bye bye !")
                break
            case _:
                print("Please choose a number between 1 and 6.")
        
        action_count += 1       
        print("Count:",action_count)
        if action_count >= 5:
            random_event(crew)
            action_count = 0  


def display_crew(crew):
    if not crew:
        print("Crew is empty !")
    else:
        for member in crew:
            print(f"First name: {member['first_name']}, Last name: {member['last_name']}, Genre: {member['gender']}, Age: {member['age']}, Role: {member['role']}")           
        print("Number of crew members:", len(crew))

def add_member(crew):
    first_name = input("first name crew : ")
    first_name = first_name.capitalize()

    last_name = input("last name crew  : ")
    last_name = last_name.capitalize()

    gender = input("Type of gender (M/F) : ")
    gender = gender.capitalize()
    

    age = int(input("Age of new crew : "))
    if age > 65:
        print("A crew member cannot be older than 65 years old.")
        return


    role = input("Role in crew : ")
    role = role.capitalize()

    for member in crew:
        if member['last_name'] == last_name:
            print("The last name must be unique.")
            return  

    while len(first_name) < 3 or len(first_name) > 15:
        print("The first name must contain between 3 and 15 characters.")
        return

    if len(last_name) < 3 or len(last_name) > 15:
        print("The last name must contain between 3 and 15 characters.")
        return
    
    if len(gender)>1:
        print("Gender must be M or F.")
        return
    
    if role == "pilot":
        if age < 25:
            print("A pilot must be older than 25 old.")
            return
        
    
    if role == "engineer":
        if age < 18:
            print("An engineer  must be older than 18 old.")
            return
        
   
        
    new_member = {
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "age": age,
        "role": role
    }
    
    crew.append(new_member)
    print(f"{first_name} {last_name} has been added to the crew.")

def remove_member(crew):
    last_name = input("Last name of member to be deleted : ")
    last_name = last_name.capitalize()

    member_found = False
    for member in crew:
        if member['last_name'] == last_name:
            crew.remove(member)
            member_found = True
            print(f"Member {last_name} has been deleted.")
            break
    
    if not member_found:
        print(f"No members with the last name '{last_name}' were found in the crew.")

def check_crew(crew):
    if len(crew) < 2:
        print("The crew must include at least 2 members.")
        return

    has_pilot = False
    has_engineer = False

    for member in crew:
        if member['role'] == 'Pilot':
            has_pilot = True
        elif member['role'] == 'Engineer': 
            has_engineer = True

    if not has_pilot:
        print("The crew must include at least a pilot.")
    
    if not has_engineer:
        print("The crew must include at least an engineer.")
    
    if has_pilot and has_engineer:
        print("The crew is ready for a new mission!")

def random_event(crew):
    event = random.choice([
        "A crew member has left the crew.",
        "A crew member has been promoted to a new role.",
        "Something unexpected happened!"
    ])

    print(f"\nRandom Event: {event}")
    if event == "A crew member has left the crew.":
        member_to_remove = random.choice(crew)
        if member_to_remove["role"] == "Commandant":
            print("You Can't remove the Commandant from the crew!")
        else:
            crew.remove(member_to_remove)
            print(f"{member_to_remove['first_name']} {member_to_remove['last_name']} has been removed from the crew.")
            
    elif event == "A crew member has been promoted to a new role.":
           
        roles = ["Doctor", "Engineer", "Pilot", "Cook", "Navigator", "Biologist", "Soldier", "Armourer", "Radio Staff","Commandant"]
    
        member_to_promote = random.choice(crew)
       
        new_role = random.choice(roles)

        if new_role == "Commandant":
            existing_commandant = any(member['role'] == "Commandant" for member in crew)
            
            if existing_commandant:
                print("There is already a Commandant in the crew. Assigning a different role.")
                new_role = random.choice([role for role in roles if role != "Commandant"])
        

        while member_to_promote['role'] == new_role:
            new_role = random.choice(roles)
        member_to_promote['role'] = new_role
        print(f"{member_to_promote['first_name']} {member_to_promote['last_name']} has been promoted to {new_role}.")    
    

    else:
        print("Something unexpected happened, but no one was affected!")
        
def crew_report(crew):
    total_members = len(crew)
    print(f"Total number of crew members: {total_members}")
    
    role_distribution = {}
    for member in crew:
        role = member['role']
        if role in role_distribution:
            role_distribution[role] += 1
        else:
            role_distribution[role] = 1
    
    print("\nRole distribution:")
    for role, count in role_distribution.items():
        print(f"{role}: {count} members")
    
    
    crew[:] = [member for member in crew if member['age'] != 65]
    
    
    max_age = 65
    close_to_max_age = [member for member in crew if member['age'] >= max_age - 5]
    
    print("\nMembers close to the maximum age >= 60 years old:")
    if close_to_max_age:
        for member in close_to_max_age:
            print(f"{member['first_name']} {member['last_name']} ({member['age']} years old) - Role: {member['role']}")
    else:
        print("No members close to the maximum age.")
    



principal_menu()


