from Person import Person  # Importation de la classe Person
from Operator import Operator  # Importation de la classe Operator
from Mentalist import Mentalist  # Importation de la classe Mentalist
from Spaceship import Spaceship  # Importation de la classe Spaceship
from Fleet import Fleet  # Importation de la classe Fleet

def add_member(spaceship, fleet):
    print("\n1. Ajouter un membre de type Person")
    print("2. Ajouter un membre de type Operator")
    print("3. Ajouter un membre de type Mentalist")
    choice = int(input("Choisissez l'option souhaitée : "))

    first_name = input("Entrez le prénom : ")
    last_name = input("Entrez le nom de famille : ")
    gender = input("Entrez le genre (M/F) : ")
    age = int(input("Entrez l'âge : "))

    if choice == 1:
        # Ajouter un membre de type Person
        new_member = Person(first_name, last_name, gender, age)
    elif choice == 2:
        # Ajouter un membre de type Operator
        role = input("Entrez le rôle (Pilote, Technicien, etc.) : ")
        experience = int(input("Entrez l'expérience (en années) : "))
        new_member = Operator(first_name, last_name, gender, age, role, experience)
    elif choice == 3:
        # Ajouter un membre de type Mentalist
        new_member = Mentalist(first_name, last_name, gender, age)
    else:
        print("Choix invalide.")
        return

    spaceship.add_member(new_member)
    fleet.add_spaceship(spaceship)  # Si nécessaire, ajoutez le vaisseau à la flotte

def remove_member(spaceship):
    last_name = input("Entrez le nom de famille du membre à supprimer : ")
    for member in spaceship.crew:
        if member.get_last_name().lower() == last_name.lower():
            spaceship.crew.remove(member)
            print(f"{member.get_first_name()} {member.get_last_name()} a été supprimé de l'équipage.")
            return
    print(f"Aucun membre trouvé avec le nom '{last_name}'.")

def display_crew(spaceship):
    if not spaceship.crew:
        print("Aucun membre d'équipage.")
        return
    print("\nÉquipage actuel :")
    for i, member in enumerate(spaceship.crew):
        print(f"- Membre {i+1}: {member.get_first_name()} {member.get_last_name()} ({member.get_role()})")

def report_crew(spaceship):
    total_members = len(spaceship.crew)
    print(f"Nombre total de l'équipage : {total_members}")
    
    role_distribution = {}
    for member in spaceship.crew:
        role = member.get_role()
        if role in role_distribution:
            role_distribution[role] += 1
        else:
            role_distribution[role] = 1
    
    print("\nDistribution des rôles dans l'équipage :")
    for role, count in role_distribution.items():
        print(f"{role}: {count} membres")
    
    # Calcul de l'expérience moyenne des opérateurs
    total_experience = 0
    operator_count = 0
    for member in spaceship.crew:
        if isinstance(member, Operator):
            operator_count += 1
            total_experience += member.get_experience()

    if operator_count > 0:
        average_experience = total_experience / operator_count
        print(f"\nNiveau moyen d'expérience des opérateurs : {average_experience:.2f}")
    else:
        print("\nAucun opérateur dans l'équipage.")

def create_spaceship():
    name = input("Entrez le nom du vaisseau : ")
    type = input("Entrez le type du vaisseau (transport, guerre, etc.) : ")
    condition = input("Entrez l'état du vaisseau (opérationnel, endommagé) : ")
    return Spaceship(name, type, condition)

def create_fleet():
    fleet_name = input("Entrez le nom de la flotte : ")
    return Fleet(fleet_name)

def menu():
    fleet = Fleet("Flotte Alpha")
    spaceship = Spaceship("Vaisseau 1", "Transport", "Opérationnel")

    while True:
        print("\nMENU :")
        print("1. Ajouter un membre")
        print("2. Supprimer un membre")
        print("3. Afficher l'équipage")
        print("4. Rapport d'équipage")
        print("5. Créer un vaisseau")
        print("6. Créer une flotte")
        print("7. Quitter")
        
        choice = int(input("Choisissez l'option souhaitée : "))

        match choice:
            case 1:
                add_member(spaceship, fleet)
            case 2:
                remove_member(spaceship)
            case 3:
                display_crew(spaceship)
            case 4:
                report_crew(spaceship)
            case 5:
                spaceship = create_spaceship()
            case 6:
                fleet = create_fleet()
            case 7:
                print("Quitter le menu.")
                break
            case _:
                print("Le choix sélectionné n'existe pas.")
