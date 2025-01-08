def main():
    crew = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "gender": "M",
            "age": 25,
            "role": "Commandant"
        },
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "gender": "F",
            "age": 24,
            "role": "Second commandant"
        },
    ]
    
    while True:
        print("\nMenu:")
        print("1. Add member")
        print("2. Delete member")
        print("3. Display crew")
        print("4. Check if the crew is ready")
        print("5. Exit")
        
        choice = input("Please select an option (1-5): ")

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
                print("bye bye !")
                break
            case _:
                print("Please choose a number between 1 and 5.")

def display_crew(crew):
    if not crew:
        print("Crew is empty !")
    else:
        for member in crew:
            print(f"First name: {member['first_name']}, Last name: {member['last_name']}, Genre: {member['gender']}, Age: {member['age']}, Role: {member['role']}")

def add_member(crew):
    first_name = input("first name crew : ")
    first_name = first_name.capitalize()

    last_name = input("last name crew  : ")
    last_name = last_name.capitalize()

    gender = input("Type of gender (M/F) : ")
    gender = gender.capitalize()

    age = int(input("Age of new crew : "))
    role = input("Role in crew : ")

    for member in crew:
        if member['last_name'] == last_name:
            print("The last name must be unique.")
            return  

    if len(first_name) < 3 or len(first_name) > 15:
        print("The first name must contain between 3 and 15 characters.")
        return

    if len(last_name) < 3 or len(last_name) > 15:
        print("The last name must contain between 3 and 15 characters.")
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
        if member['role'].lower() == 'pilot':
            has_pilot = True
        elif member['role'].lower() == 'engineer': 
            has_engineer = True

    if not has_pilot:
        print("The crew must include at least one pilot.")
    
    if not has_engineer:
        print("The crew must include at least one engineer.")
    
    if has_pilot and has_engineer:
        print("The crew is ready for the mission!")



main()
