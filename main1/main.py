from Person import Person
from Operator import Operator
from Mentalist import Mentalist
from Spaceship import Spaceship
from Fleet import Fleet

def add_person(crew):
    print("Création d'un nouveau membre d'équipage (Personne Générique)")
    first_name = input("Prénom : ")
    last_name = input("Nom : ")
    gender = input("Genre (M/F) : ")
    age = int(input("Âge : "))
    person = Person(first_name, last_name, gender, age)
    crew.append(person)
    print(f"{first_name} {last_name} ajouté à l'équipage en tant que personne générique.")

def add_operator(crew):
    print("Création d'un nouvel opérateur (Technicien/Pilote)")
    first_name = input("Prénom : ")
    last_name = input("Nom : ")
    gender = input("Genre (M/F) : ")
    age = int(input("Âge : "))
    role = input("Rôle (pilote/technicien) : ")
    operator = Operator(first_name, last_name, gender, age, role)
    crew.append(operator)
    print(f"{first_name} {last_name} ajouté à l'équipage en tant qu'{role}.")

def add_mentalist(crew):
    print("Création d'un mentaliste")
    first_name = input("Prénom : ")
    last_name = input("Nom : ")
    gender = input("Genre (M/F) : ")
    age = int(input("Âge : "))
    mentalist = Mentalist(first_name, last_name, gender, age)
    crew.append(mentalist)
    print(f"{first_name} {last_name} ajouté à l'équipage en tant que mentaliste.")

def display_crew(crew):
    if not crew:
        print("L'équipage est vide.")
    else:
        for member in crew:
            print(f"{member.first_name} {member.last_name} - {member.__class__.__name__} ({member.age} ans)")
            print(f"  - {member.introduce_yourself()}")

def crew_action(crew):
    if not crew:
        print("L'équipage est vide.")
        return
    for i, member in enumerate(crew, 1):
        print(f"{i}. {member.first_name} {member.last_name} ({member.__class__.__name__})")
    choice = int(input("Choisissez un membre (numéro) pour effectuer une action : "))
    member = crew[choice - 1]
    
    if isinstance(member, Operator):
        action = input("Choisissez une action : [act] pour agir, [promote] pour promouvoir : ")
        if action == "act":
            member.act()
        elif action == "promote":
            member.promote()
        else:
            print("Action non reconnue.")
    elif isinstance(member, Mentalist):
        action = input("Choisissez une action : [act] pour agir, [recharge] pour recharger le mana : ")
        if action == "act":
            target_name = input("Ciblez un membre (nom) : ")
            target = next((m for m in crew if m.first_name == target_name), None)
            if target:
                member.act(target)
            else:
                print("Cible non trouvée.")
        elif action == "recharge":
            member.recharge_mana()
        else:
            print("Action non reconnue.")
    else:
        print(f"Aucune action n'est définie pour {member.__class__.__name__}.")

def add_spaceship(fleet):
    name = input("Nom du vaisseau : ")
    ship_type = input("Type du vaisseau (transport, guerre, marchand) : ")
    spaceship = Spaceship(name, ship_type)
    fleet.add_spaceship(spaceship)

def add_member_to_spaceship(fleet):
    if not fleet.spaceships:
        print("Aucune flotte disponible.")
        return
    print("Sélectionnez un vaisseau:")
    for i, spaceship in enumerate(fleet.spaceships, 1):
        print(f"{i}. {spaceship.name}")
    choice = int(input("Choisissez un vaisseau (numéro) : ")) - 1
    spaceship = fleet.spaceships[choice]

    print("Sélectionnez un membre à ajouter (personne générique, opérateur, mentaliste) :")
    member_type = input("Entrez 'person' pour une personne, 'operator' pour un opérateur, 'mentalist' pour un mentaliste : ")

    if member_type == 'person':
        add_person(spaceship.crew)
    elif member_type == 'operator':
        add_operator(spaceship.crew)
    elif member_type == 'mentalist':
        add_mentalist(spaceship.crew)
    else:
        print("Type de membre inconnu.")

def check_fleet_preparation(fleet):
    if not fleet.spaceships:
        print("Aucune flotte disponible.")
        return
    for spaceship in fleet.spaceships:
        spaceship.check_preparation()

def main():
    print("Le programme commence ici.")  # Message pour vérifier que la fonction main() est atteinte
    crew = []
    fleet = Fleet("Flotte Alpha")
    while True:
        print("\nMenu principal :")
        print("1. Ajouter une personne générique à l'équipage")
        print("2. Ajouter un opérateur (pilote/technicien) à l'équipage")
        print("3. Ajouter un mentaliste à l'équipage")
        print("4. Afficher l'équipage")
        print("5. Effectuer une action sur un membre de l'équipage")
        print("6. Ajouter un vaisseau à la flotte")
        print("7. Ajouter un membre à un vaisseau")
        print("8. Vérifier la préparation de la flotte")
        print("9. Quitter")
        
        choice = input("Choisissez une option : ")

        match choice:
            case "1":
                add_person(crew)
            case "2":
                add_operator(crew)
            case "3":
                add_mentalist(crew)
            case "4":
                display_crew(crew)
            case "5":
                crew_action(crew)
            case "6":
                add_spaceship(fleet)
            case "7":
                add_member_to_spaceship(fleet)
            case "8":
                check_fleet_preparation(fleet)
            case "9":
                print("Au revoir!")
                break
            case _:from Person import Person
from Operator import Operator
from Mentalist import Mentalist
from Spaceship import Spaceship
from Fleet import Fleet

# Ajout d'une personne à l'équipage
def add_person(crew):
    print("Création d'un nouveau membre d'équipage (Personne Générique)")
    first_name = input("Prénom : ")
    last_name = input("Nom : ")
    gender = input("Genre (M/F) : ")
    age = int(input("Âge : "))
    person = Person(first_name, last_name, gender, age)
    crew.append(person)
    print(f"{first_name} {last_name} ajouté à l'équipage en tant que personne générique.")

# Ajouter un opérateur à l'équipage
def add_operator(crew):
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
def add_mentalist(crew):
    print("Création d'un mentaliste")
    first_name = input("Prénom : ")
    last_name = input("Nom : ")
    gender = input("Genre (M/F) : ")
    age = int(input("Âge : "))
    mentalist = Mentalist(first_name, last_name, gender, age)
    crew.append(mentalist)
    print(f"{first_name} {last_name} ajouté à l'équipage en tant que mentaliste.")

# Afficher l'équipage
def display_crew(crew):
    if not crew:
        print("L'équipage est vide.")
    else:
        for member in crew:
            print(f"{member.first_name} {member.last_name} - {member.__class__.__name__} ({member.age} ans)")
            print(f"  - {member.introduce_yourself()}")

# Effectuer une action sur un membre de l'équipage
def crew_action(crew):
    if not crew:
        print("L'équipage est vide.")
        return
    for i, member in enumerate(crew, 1):
        print(f"{i}. {member.first_name} {member.last_name} ({member.__class__.__name__})")
    choice = int(input("Choisissez un membre (numéro) pour effectuer une action : "))
    member = crew[choice - 1]
    
    if isinstance(member, Operator):
        action = input("Choisissez une action : [act] pour agir, [promote] pour promouvoir : ")
        if action == "act":
            member.act()
        elif action == "promote":
            member.promote()
        else:
            print("Action non reconnue.")
    elif isinstance(member, Mentalist):
        action = input("Choisissez une action : [act] pour agir, [recharge] pour recharger le mana : ")
        if action == "act":
            target_name = input("Ciblez un membre (nom) : ")
            target = next((m for m in crew if m.first_name == target_name), None)
            if target:
                member.act(target)
            else:
                print("Cible non trouvée.")
        elif action == "recharge":
            member.recharge_mana()
        else:
            print("Action non reconnue.")
    else:
        print(f"Aucune action n'est définie pour {member.__class__.__name__}.")

# Ajouter un vaisseau à la flotte
def add_spaceship(fleet):
    name = input("Nom du vaisseau : ")
    ship_type = input("Type du vaisseau (transport, guerre, marchand) : ")
    spaceship = Spaceship(name, ship_type)
    fleet.add_spaceship(spaceship)

# Ajouter un membre à un vaisseau
def add_member_to_spaceship(fleet):
    if not fleet.spaceships:
        print("Aucune flotte disponible.")
        return
    print("Sélectionnez un vaisseau:")
    for i, spaceship in enumerate(fleet.spaceships, 1):
        print(f"{i}. {spaceship.name}")
    choice = int(input("Choisissez un vaisseau (numéro) : ")) - 1
    spaceship = fleet.spaceships[choice]

    print("Sélectionnez un membre à ajouter (personne générique, opérateur, mentaliste) :")
    member_type = input("Entrez 'person' pour une personne, 'operator' pour un opérateur, 'mentalist' pour un mentaliste : ")

    if member_type == 'person':
        add_person(spaceship.crew)
    elif member_type == 'operator':
        add_operator(spaceship.crew)
    elif member_type == 'mentalist':
        add_mentalist(spaceship.crew)
    else:
        print("Type de membre inconnu.")

# Vérifier la préparation de la flotte
def check_fleet_preparation(fleet):
    if not fleet.spaceships:
        print("Aucune flotte disponible.")
        return
    for spaceship in fleet.spaceships:
        spaceship.check_preparation()

# Point d'entrée du programme
def main():
    crew = []
    fleet = Fleet("Flotte Alpha")
    while True:
        print("\nMenu principal :")
        print("1. Ajouter une personne générique à l'équipage")
        print("2. Ajouter un opérateur (pilote/technicien) à l'équipage")
        print("3. Ajouter un mentaliste à l'équipage")
        print("4. Afficher l'équipage")
        print("5. Effectuer une action sur un membre de l'équipage")
        print("6. Ajouter un vaisseau à la flotte")
        print("7. Ajouter un membre à un vaisseau")
        print("8. Vérifier la préparation de la flotte")
        print("9. Quitter")
        
        choice = input("Choisissez une option : ")

        match choice:
            case "1":
                add_person(crew)
            case "2":
                add_operator(crew)
            case "3":
                add_mentalist(crew)
            case "4":
                display_crew(crew)
            case "5":
                crew_action(crew)
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

                print("Option invalide.")

if __name__ == "__main__":
    main()
