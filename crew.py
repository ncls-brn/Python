

## list of crew 

crew = [
  {
    "first_name": "John",
    "last_name": "Doe",
    "gender":"M",
    "age": 25,
    "role" : "Commandant"
  },
  {
    "first_name": "Jane",
    "last_name": "Doe",
    "gender":"F",
    "age": 24,
    "role" : "Second commandant"
  },
]


def display_crew(crew):
    if not crew:
        print("Crew is empty !")
    else:
        
        for member in crew:
            print(f"First name: {member['first_name']}, Last name: {member['last_name']}, Genre: {member['gender']}, Age: {member['age']}, Role: {member['role']}")


# function to add new crew 

def add_member(crew):
    
    first_name = input("first name crew : ")
    last_name = input("last name crew  : ")
    gender = input("Type of gender (M/F) : ")
    age = int(input("Age of new crew : "))
    role = input("Role in crew : ")

   
    for member in crew:
        if member['last_name'] == last_name:
            print("the last name must be unique.")
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




add_member(crew)
remove_member(crew)
display_crew(crew)