from Person import Person
from Operator import Operator
from Mentalist import Mentalist
from Spaceship import Spaceship
from Fleet import Fleet
import json

# Liste globale des membres d'équipage
crew = []

def save_data(fleet, crew):
    # Crée un dictionnaire pour contenir toutes les données
    data = {
        "crew": [{
            "first_name": member.get_first_name(),
            "last_name": member.get_last_name(),
            "gender": member.get_gender(),
            "age": member.get_age(),
            "role": getattr(member, 'get_role', lambda: 'Non spécifié')()  # Si l'objet n'a pas de méthode get_role, retourne 'Non spécifié'
        } for member in crew],

        "spaceships": [{
            "name": spaceship.name,
            "ship_type": spaceship.type,  # Utilisation de 'type' pour le type de vaisseau
            "condition": spaceship.condition,
            "crew": [{
                "first_name": member.get_first_name(),
                "last_name": member.get_last_name(),
                "gender": member.get_gender(),
                "age": member.get_age(),
                "role": getattr(member, 'get_role', lambda: 'Non spécifié')()  # Si l'objet n'a pas de méthode get_role, retourne 'Non spécifié'
            } for member in spaceship.crew]
        } for spaceship in fleet.spaceships]
    }

    # Sauvegarde les données dans un fichier JSON
    try:
        with open("./data.json", "w") as f:
            json.dump(data, f)  # Utilisation de json.dump pour écrire dans le fichier JSON
        print("Données sauvegardées avec succès.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des données: {e}")


   
def load_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)

        # Charger les membres d'équipage
        crew = []
        for member_data in data.get("crew", []):
            if member_data["role"]:  # Si c'est un opérateur
                member = Operator(
                    member_data["first_name"],
                    member_data["last_name"],
                    member_data["gender"],
                    member_data["age"],
                    member_data["role"]
                )
            else:  # C'est une personne générique
                member = Person(
                    member_data["first_name"],
                    member_data["last_name"],
                    member_data["gender"],
                    member_data["age"]
                )
            crew.append(member)

        # Charger les vaisseaux et leur équipage
        fleet = Fleet("Flotte Alpha")
        for spaceship_data in data.get("spaceships", []):
            spaceship = Spaceship(
                spaceship_data["name"],
                spaceship_data["ship_type"],
                spaceship_data["condition"]
            )
            for member_data in spaceship_data["crew"]:
                # Ajouter les membres du vaisseau
                member = next((m for m in crew if m.first_name == member_data["first_name"] and m.last_name == member_data["last_name"]), None)
                if member:
                    spaceship.add_member(member)
            fleet.add_spaceship(spaceship)

        print("Données chargées avec succès.")
        return fleet, crew
    except FileNotFoundError:
        print("Aucun fichier de sauvegarde trouvé. Démarrage avec un nouveau jeu.")
        return Fleet("Flotte Alpha"), []  # Retourner une flotte vide et un équipage vide si le fichier n'existe pas

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

def check_fleet_preparation(fleet):
    if not fleet.spaceships:
        print("Aucune flotte disponible.")
        return
    
    for spaceship in fleet.spaceships:
        # Afficher les détails de l'équipage du vaisseau
        spaceship.display_crew_details()  # Affiche les détails de l'équipage

        # Vérifier si le vaisseau est prêt pour la mission
        pilots = [m for m in spaceship.crew if isinstance(m, Operator) and m.role == "pilote"]
        technicians = [m for m in spaceship.crew if isinstance(m, Operator) and m.role == "technicien"]
        mentalists = [m for m in spaceship.crew if isinstance(m, Mentalist) and m.mana >= 50]

        if pilots and technicians and mentalists:
            print(f"Le vaisseau {spaceship.name} est prêt pour la mission.")
        else:
            print(f"Le vaisseau {spaceship.name} n'est pas prêt. Il manque des membres essentiels.")

# Point d'entrée du programme
def main():
    # Charger les données depuis le fichier JSON au démarrage
    fleet, crew = load_data()

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
                # Sauvegarder les données avant de quitter
                save_data(fleet, crew)
                print("Au revoir!")
                break
            case _:
                print("Option invalide.")

if __name__ == "__main__":
    main()
