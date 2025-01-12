def add_member(crew):
    first_name = input("Prénom du membre d’équipage : ")
    last_name = input("Nom de famille du membre d’équipage : ")
    gender = input("Genre du membre (M/F) : ")
    age = int(input("Âge du membre : "))
    role = input("Rôle du membre (pilote/technicien) : ")

    if 3 <= len(first_name) <= 15 and 3 <= len(last_name) <= 15:
        new_member = {
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "age": age,
            "role": role
        }
        # Vérification si le nom est unique
        for member in crew:
            if member["last_name"] == last_name:
                print("Erreur : Le nom de famille existe déjà.")
                return
        crew.append(new_member)
        print(f"{first_name} {last_name} ajouté à l'équipage.")
    else:
        print("Erreur : Le prénom et nom doivent contenir entre 3 et 15 caractères.")

def remove_member(crew):
    last_name = input("Nom de famille du membre à supprimer : ")
    for member in crew:
        if member["last_name"] == last_name:
            crew.remove(member)
            print(f"{last_name} a été retiré de l'équipage.")
            return
    print("Erreur : Nom de famille introuvable.")

def display_crew(crew):
    if crew:
        for member in crew:
            print(f"{member['first_name']} {member['last_name']} - {member['role']} ({member['age']} ans)")
    else:
        print("L'équipage est vide.")

def check_crew(crew):
    if len(crew) >= 2:
        pilots = [m for m in crew if m['rRôle'] == "pilote"]
        technicians = [m for m in crew if m['Rôle'] == "technicien"]
        if pilots and technicians:
            print("L’équipage est prêt pour la mission !")
        else:
            print("L’équipage n'est pas prêt. Il manque un pilote ou un technicien.")
    else:
        print("L’équipage doit contenir au moins 2 membres.")
def remove_member(crew):
    last_name = input("Nom de famille du membre à supprimer : ")
    for member in crew:
        if member["last_name"] == last_name:
            crew.remove(member)
            print(f"{last_name} a été retiré de l'équipage.")
            return
    print("Erreur : Nom de famille introuvable.")
