def add_member(crew):
    first_name = input("Entrez le prénom du nouveau membre d'équipage : ")
    while len(first_name) < 3 or len(first_name) > 15:
        first_name = input("Le prénom doit faire entre 3 et 15 caractères, réessayez : ")

    last_name = input("Entrez le nom de famille du nouveau membre d'équipage : ")
    while len(last_name) < 3 or len(last_name) > 15:
        last_name = input("Le nom de famille doit faire entre 3 et 15 caractères, réessayez : ")
    while not is_unique_last_name(last_name, crew):
        last_name = input("Le nom de famille est déjà existant, réessayez : ")

    gender = input("Entrez le genre du nouveau membre d'équipage : ")
    age = int(input("Entrez l'âge du nouveau membre d'équipage : "))
    role = input("Entrez le rôle du nouveau membre d'équipage : ")

    new_member = {
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "age": age,
        "role": role,
    }
    crew.append(new_member)


def is_unique_last_name(last_name, crew):
    for member in crew:
        if last_name.lower() == member["last_name"].lower():
            return False
    return True


def remove_member(crew):
    if is_empty(crew):
        print("Aucun membre d'équipage.")
        return
    last_name = input("Entrez le nom de famille du membre à supprimer : ")
    for member in crew:
        if member["last_name"].lower() == last_name.lower():
            crew.remove(member)
            print(f"{member['first_name']} {member['last_name']} a bien été supprimé")
            return
    print("Nom inconnu dans l'équipage")


def display_crew(crew):
    if is_empty(crew):
        print("Aucun membre d'équipage.")
        return
    for i, member in enumerate(crew):
        print("-" * 100)
        print(f"Membre numéro {i+1} : ")
        display_member(member)


def display_member(member):
    print(f"Prénom : {member['first_name']}")
    print(f"Nom de famille : {member['last_name']}")
    print(f"Genre : {member['gender']}")
    print(f"Âge : {member['age']}")
    print(f"Rôle : {member['role']}")


def is_empty(crew):
    return not crew


def check_crew(crew):
    if is_empty(crew):
        print("Aucun membre d'équipage.")
        return
    if len(crew) < 2:
        print("L'équipage doit contenir au moins deux membres pour partir en mission")
        return
    have_pilot = False
    have_technician = False
    for member in crew:
        if member["role"].lower() == "pilote":
            have_pilot = True
        elif member["role"].lower() == "technicien":
            have_technician = True
        if have_pilot and have_technician:
            break
    if not have_pilot:
        print("Il manque un pilote pour la mission.")
    if not have_technician:
        print("Il manque un technicien pour la mission.")
    if have_pilot and have_technician:
        print("L'équipage est prêt pour la mission !")
    else:
        print("L'équipage n'est pas complet pour la mission !")


def crew_report(crew):
    total_members = len(crew)
    print(f"Nombre total de l'équipage : {total_members}")
    
    role_distribution = {}
    for member in crew:
        role = member['role']
        if role in role_distribution:
            role_distribution[role] += 1
        else:
            role_distribution[role] = 1
    
    print("\nDistribution des rôles:")
    for role, count in role_distribution.items():
        print("-" * 25)
        print(f"{role}: {count} membres")
        
    
    
    crew[:] = [member for member in crew if member['age'] != 65]
    
    
    max_age = 65
    close_to_max_age = [member for member in crew if member['age'] >= max_age - 5]
    
    print("\nMembres proche de l'age maximum >= 60ans:")
    if close_to_max_age:
        for member in close_to_max_age:
            print(f"{member['first_name']} {member['last_name']} ({member['age']} ans) - Role: {member['role']}")
    else:
        print("Aucun membres n'est proche de l'age de la retraite.")
    
