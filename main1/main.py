from Person import Person
from Operator import Operator
from Mentalist import Mentalist
from Spaceship import Spaceship
from Fleet import Fleet

# Liste globale des membres d'équipage
crew = []

# Ajout d'une personne générique à l'équipage
def add_person():
    print("Création d'un nouveau membre d'équipage (Personne Générique)")
    first_name = input("Prénom : ")
    last_name = input("Nom : ")
    gender = input("Genre (M/F) : ")
    age = int(input("Âge : "))
    person = Person(first_name, last_name, gender, age)
    crew.append(person)
    print(f"{first_name} {last_name} ajouté à l'équipage en tant que personne générique.")

# Ajouter un opérateur à l'équipage
def add_operator():
    print("Création d'un nouvel opérateur (Technicien/Pilote)")
    first_name = input("Prénom : ")
    last_name = input("Nom : ")
    gender = input("Genre (M/F) : ")
    age = int(input("Âge : "))
    role = input("Rôle (pilote/technicien) : ")
    operator = Operator(first_name, last_name, gender, age, role)
    crew.append(operator)
    print(f"{first_name} {last_name} ajouté à l'équipage en tant qu'{role}.")

# Ajouter un mentaliste à l'équipage
def add_mentalist():
    print("Création d'un mentaliste")
    first_name = input("Prénom : ")
    last_name = input("Nom : ")
    gender = input("Genre (M/F) : ")
    age = int(input("Âge : "))
    mentalist = Mentalist(first_name, last_name, gender, age)
    crew.append(mentalist)
    print(f"{first_name} {last_name} ajouté à l'équipage en tant que mentaliste.")

# Afficher l'équipage
def display_crew():
    if not crew:
        print("L'équipage est vide.")
    else:
        for i, member in enumerate(crew, 1):
            print(f"{i}. {member.first_name} {member.last_name} - {member.__class__.__name__} ({member.age} ans)")
            print(f"  - {member.introduce_yourself()}")

# Ajouter un membre à un vaisseau spécifique
def add_member_to_spaceship(fleet):
    if not fleet.spaceships:
        print("Aucune flotte disponible.")
        return

    print("Sélectionnez un vaisseau:")
    for i, spaceship in enumerate(fleet.spaceships, 1):
        print(f"{i}. {spaceship.name}")
    choice = int(input("Choisissez un vaisseau (numéro) : ")) - 1
    spaceship = fleet.spaceships[choice]

    # Afficher la liste des membres existants dans l'équipage
    print("Sélectionnez un membre à ajouter au vaisseau:")
    if not crew:
        print("Aucun membre disponible dans l'équipage.")
        return

    for i, member in enumerate(crew, 1):
        print(f"{i}. {member.first_name} {member.last_name} - {member.__class__.__name__} ({member.age} ans)")
    
    choice = int(input("Choisissez un membre (numéro) : ")) - 1
    member_to_add = crew[choice]

    # Ajouter le membre sélectionné au vaisseau
    spaceship.add_member(member_to_add)

    # Supprimer le membre ajouté de la liste `crew` pour qu'il ne soit plus disponible
    del crew[choice]
    print(f"{member_to_add.first_name} {member_to_add.last_name} a été ajouté au vaisseau {spaceship.name} et supprimé de l'équipage.")


# Effectuer des actions sur un membre du vaisseau
def crew_action(fleet):
    if not fleet.spaceships:
        print("Aucun vaisseau dans la flotte.")
        return

    # Sélectionner un vaisseau de la flotte
    print("Sélectionnez un vaisseau:")
    for i, spaceship in enumerate(fleet.spaceships, 1):
        print(f"{i}. {spaceship.name}")
    
    choice = int(input("Choisissez un vaisseau (numéro) : ")) - 1
    spaceship = fleet.spaceships[choice]

    if not spaceship.crew:
        print(f"Le vaisseau {spaceship.name} n'a pas d'équipage.")
        return

    # Afficher la liste des membres du vaisseau
    print(f"\nMembres de l'équipage du vaisseau {spaceship.name}:")
    for i, member in enumerate(spaceship.crew, 1):
        print(f"{i}. {member.first_name} {member.last_name} - {member.__class__.__name__} ({member.age} ans)")

    choice = int(input("Choisissez un membre (numéro) pour effectuer une action : ")) - 1
    member_to_act = spaceship.crew[choice]

    # Effectuer l'action en fonction du type de membre
    if isinstance(member_to_act, Operator):
        action = input("Choisissez une action : [act] pour agir, [promote] pour promouvoir : ")
        if action == "act":
            member_to_act.act()
        elif action == "promote":
            member_to_act.promote()
        else:
            print("Action non reconnue.")
    elif isinstance(member_to_act, Mentalist):
        action = input("Choisissez une action : [act] pour agir, [recharge] pour recharger le mana : ")
        if action == "act":
            target_name = input("Ciblez un membre du vaisseau (nom) : ")
            target = next((m for m in spaceship.crew if m.first_name == target_name), None)
            if target:
                member_to_act.act(target)
            else:
                print("Cible non trouvée.")
        elif action == "recharge":
            member_to_act.recharge_mana()
        else:
            print("Action non reconnue.")
    else:
        print(f"Aucune action définie pour le membre {member_to_act.__class__.__name__}.")

# Ajouter un vaisseau à la flotte
def add_spaceship(fleet):
    name = input("Nom du vaisseau : ")
    ship_type = input("Type du vaisseau (transport, guerre, marchand) : ")
    spaceship = Spaceship(name, ship_type)
    fleet.add_spaceship(spaceship)

# Vérifier la préparation de la flotte
def check_fleet_preparation(fleet):
    if not fleet.spaceships:
        print("Aucune flotte disponible.")
        return
    for spaceship in fleet.spaceships:
        spaceship.check_preparation()

# Point d'entrée du programme
def main():
    fleet = Fleet("Alpha")
    
    while True:
        print("\nMenu principal :")
        print("1. Ajouter une personne générique à l'équipage")
        print("2. Ajouter un opérateur (pilote/technicien) à l'équipage")
        print("3. Ajouter un mentaliste à l'équipage")
        print("4. Afficher l'équipage")
        print("5. Effectuer une action sur un membre du vaisseau")
        print("6. Ajouter un vaisseau à la flotte")
        print("7. Ajouter un membre à un vaisseau")
        print("8. Vérifier la préparation de la flotte")
        print("9. Quitter")
        
        choice = input("Choisissez une option : ")

        match choice:
            case "1":
                add_person()
            case "2":
                add_operator()
            case "3":
                add_mentalist()
            case "4":
                display_crew()
            case "5":
                crew_action(fleet)
            case "6":
                add_spaceship(fleet)
            case "7":
                add_member_to_spaceship(fleet)
            case "8":
                check_fleet_preparation(fleet)
            case "9":
                print("Au revoir!")
                break
            case _:
                print("Option invalide.")

if __name__ == "__main__":
    main()
