from Person import Person
from Operator import Operator
from Mentalist import Mentalist
from Spaceship import Spaceship
from Fleet import Fleet
import json


crews = []

# Ajout d'une personne générique à l'équipage
def add_person():
    print("Création d'un nouveau membre d'équipage (Personne Civil)")

    # Demander le prénom
    first_name = input("Prénom : ")
    while len(first_name) < 3 or len(first_name) > 15:
        print("Le prénom doit contenir entre 3 et 15 caractères")
        first_name = input("Prénom (entre 3 et 15 caractères) : ")

    # Demander le nom de famille
    last_name = input("Nom : ")
    while len(last_name) < 3 or len(last_name) > 15:
        print("Le nom de famille doit contenir entre 3 et 15 caractères")
        last_name = input("Nom (entre 3 et 15 caractères) : ")

    # Demander le genre
    gender = input("Genre (M/F) : ")
    
    # Demander l'âge et vérifier qu'il ne dépasse pas 65
    age = int(input("Âge : "))
    while age > 65:
        print("Aucun membre ne peut avoir plus de 65 ans...")
        age = int(input("Âge (maximum 65 ans) : "))

    # Vérifier si le nom de famille est unique
    for member in crews:
        if member.last_name.lower() == last_name.lower():
            print("Le nom de famille doit être unique.")
            return

    # Créer la personne et l'ajouter à l'équipage
    person = Person(first_name, last_name, gender, age)
    crews.append(person)
    print(f"{first_name} {last_name} ajouté à l'équipage en tant que personne civil.")

# Ajouter un opérateur à l'équipage
def add_operator():
    print("Création d'un nouvel opérateur (Technicien/Pilote)")
    first_name = input("Prénom : ")
    while len(first_name) < 3 or len(first_name) > 15:
        print("Le prénom doit contenir entre 3 et 15 caracteres")
        return
    last_name = input("Nom : ")
    while len(last_name) < 3 or len(last_name) > 15:
        print("Le nom de famille doit contenir entre 3 et 15 caracteres")
        return
    gender = input("Genre (M/F) : ")
    age = int(input("Âge : "))
    if age > 65:
        print("Aucun membre ne peut avoir plus de 65ans...")
        return
    role = input("Rôle (pilote/technicien) : ")
    if role == "pilote":
        if age < 25:
            print("le pilote doit etre agé de plus de 25ans!")
            return
    if role == "technicien":
        if age < 18:
            print("le pilote doit etre agé de plus de 18ans!")
            return 
          
    for member in crews:
        if member.last_name.lower() == last_name.lower():
            print("Le nom de famille doit être unique.")
            return           
    operator = Operator(first_name, last_name, gender, age, role)
    crews.append(operator)
    print(f"{first_name} {last_name} ajouté à l'équipage en tant qu'{role}.")

# Ajouter un mentaliste à l'équipage
def add_mentalist():
    print("Création d'un mentaliste")
    first_name = input("Prénom : ")
    while len(first_name) < 3 or len(first_name) > 15:
        print("Le prénom doit contenir entre 3 et 15 caracteres")
        return
    last_name = input("Nom : ")
    while len(last_name) < 3 or len(last_name) > 15:
        print("Le nom de famille doit contenir entre 3 et 15 caracteres")
        return
    gender = input("Genre (M/F) : ")
    age = int(input("Âge : "))
    if age > 65:
        print("Aucun membre ne peut avoir plus de 65ans...")
        return
      
    for member in crews:
        if member.last_name.lower() == last_name.lower():
            print("Le nom de famille doit être unique.")
            return  
    mentalist = Mentalist(first_name, last_name, gender, age)
    
    crews.append(mentalist)
    print(f"{first_name} {last_name} ajouté à l'équipage en tant que mentaliste.")

# Afficher l'équipage
def display_crew():
    if not crews:
        print("L'équipage au sol est vide.")
    else:
        for i, member in enumerate(crews, 1):
            print(f"{i}. {member.first_name} {member.last_name} - {member.role} ({member.age} ans)")
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
    if not crews:
        print("Aucun membre disponible dans l'équipage.")
        return

    for i, member in enumerate(crews, 1):
        print(f"{i}. {member.first_name} {member.last_name} - {member.role} ({member.age} ans)")
    
    choice = int(input("Choisissez un membre (numéro) : ")) - 1
    member_to_add = crews[choice]

    # Ajouter le membre sélectionné au vaisseau
    spaceship.add_member(member_to_add)

    # Supprimer le membre ajouté de la liste `crew` pour qu'il ne soit plus disponible
    del crews[choice]
    print(f"{member_to_add.first_name} {member_to_add.last_name} a été ajouté au vaisseau {spaceship.name} et supprimé de l'équipage au sol.")

# Effectuer des actions sur un membre du vaisseau
def crew_action(fleet):
    if not fleet.spaceships:
        print("Aucun vaisseau dans la flotte.")
        return

    # Sélectionner un vaisseau de la flotte
    print("Sélectionnez un vaisseau:")
    for i, spaceship in enumerate(fleet.spaceships, 1):
        print(f"{i}. {spaceship.name}")
    
    try:
        choice = int(input("Choisissez un vaisseau (numéro) : ")) - 1
        spaceship = fleet.spaceships[choice]
    except (ValueError, IndexError):
        print("Choix invalide. Veuillez entrer un numéro valide.")
        return

    # Vérifier si le vaisseau a un équipage
    if not spaceship.crew:  # Utilisation de l'attribut crew directement
        print(f"Le vaisseau {spaceship.name} n'a pas d'équipage.")
        return

    # Afficher la liste des membres du vaisseau
    print(f"\nMembres de l'équipage du vaisseau {spaceship.name}:")
    for i, member in enumerate(spaceship.crew, 1):  # Utilisation de l'attribut crew
        print(f"{i}. {member.first_name} {member.last_name} - {member.role} ({member.age} ans)")

    try:
        choice = int(input("Choisissez un membre (numéro) pour effectuer une action : ")) - 1
        member_to_act = spaceship.crew[choice]  # Utilisation de l'attribut crew
    except (ValueError, IndexError):
        print("Choix invalide. Veuillez entrer un numéro valide.")
        return

    # Effectuer l'action en fonction du type de membre
    if isinstance(member_to_act, Operator):
        action = input("Choisissez une action : [piloter] pour piloter, [maintenance] pour effectuer une maintenance, [act] pour agir : ")
        
        if action == "piloter":
            print(f"{member_to_act.first_name} {member_to_act.last_name} pilote le vaisseau.")
            member_to_act.gain_experience()  # Augmente l'expérience pour le pilote
        elif action == "maintenance":
            print(f"{member_to_act.first_name} {member_to_act.last_name} effectue la maintenance du vaisseau.")
            member_to_act.gain_experience()  # Augmente l'expérience pour le technicien
        elif action == "act":
            member_to_act.act()
        else:
            print("Action non reconnue.")
    elif isinstance(member_to_act, Mentalist):
        action = input("Choisissez une action : [act] pour agir, [recharge] pour recharger le mana : ")

        # Vérification du mana du Mentalist avant d'agir
        if member_to_act.mana <= 19:
            print(f"{member_to_act.first_name} {member_to_act.last_name} n'a pas assez de mana pour agir.")
            if action == "recharge":
                member_to_act.recharge_mana()  # Recharger le mana
            return  # Si le mana est insuffisant, ne pas continuer l'action

        if action == "act":
            target_name = input("Ciblez un membre du vaisseau (nom) : ")
            target = next((m for m in spaceship.crew if m.first_name == target_name), None)  # Utilisation de `first_name`
            
            if target:
                member_to_act.act(target)

                # Si le membre ciblé est un opérateur (pilote ou technicien), il perd 1 point d'expérience
                if isinstance(target, Operator):       
                    if target.experience > 0:  # Si le pilote ou technicien a de l'expérience
                        target.experience -= 1
                        print(f"{target.first_name} {target.last_name} perd 1 point d'expérience.")
                    else:
                        print(f"{target.first_name} {target.last_name} n'a pas assez d'expérience pour en perdre.")
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
    ship_condition = input("Condition du vaisseau (operatonnel, endommage) : ")
    spaceship = Spaceship(name, ship_type, ship_condition)
    fleet.add_spaceship(spaceship)

# Vérifier la préparation de la flotte et afficher les détails de l'équipage
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


def remove_member(crew):
    last_name = input("Nom de famille du membre à supprimer : ")
    
    # Recherche dans l'équipage
    for member in crew:
        if member.last_name.lower() == last_name.lower():
            crew.remove(member)
            print(f"{last_name} a été retiré de l'équipage.")
            return
    print("Erreur : Nom de famille introuvable.")


def display_spaceships(fleet):
    if not fleet.spaceships:
        print("Aucun vaisseau dans la flotte.")
    else:
        print("\nListe des vaisseaux dans la flotte :")
        for i, spaceship in enumerate(fleet.spaceships, 1):
            print(f"{i}. {spaceship.name} - Type : {spaceship.ship_type} - Condition : {spaceship.condition}")
            print("  Équipage :")
            if spaceship.crew:
                for member in spaceship.crew:
                    print(f"    {member.first_name} {member.last_name} - {member.role} ({member.age} ans)")
            else:
                print("  Aucun membre d'équipage.")

        
def save_data(fleet, crew, file_name="./main1/data.json"):
    data = {
        "crew": [member.to_dict() for member in crew],  
        "spaceships": [spaceship.to_dict() for spaceship in fleet.spaceships]
    }

    print("Données à sauvegarder:", data)  

    try:
        with open(file_name, "w") as f:
            json.dump(data, f, indent=4) 
        print(f"Données sauvegardées avec succès dans {file_name}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des données: {e}")  


def load_data(file_name="./main1/data.json"):
    try:
        with open(file_name, "r") as f:
            data = json.load(f)
        
        fleet = Fleet("Flotte Alpha")
        
        # Charger les membres de l'équipage au sol (crews)
        global crews
        crews = []  # Initialiser la liste des membres au sol
        for member_data in data.get("crew", []):
            role = member_data.get("role") or member_data.get("Rôle")  # Gestion des variations de clé 'role'
            
            if role == "civil":
                member = Person(
                    member_data["first_name"],
                    member_data["last_name"],
                    member_data["gender"],
                    member_data["age"]
                )
            elif role == "pilote" or role == "technicien":
                member = Operator(
                    member_data["first_name"],
                    member_data["last_name"],
                    member_data["gender"],
                    member_data["age"],
                    role  # Le rôle sera "pilote" ou "technicien"
                )
            elif role == "mentalist":
                member = Mentalist(
                    member_data["first_name"],
                    member_data["last_name"],
                    member_data["gender"],
                    member_data["age"]
                )
            else:
                print(f"Rôle inconnu : {role}. Impossible de charger ce membre.")
                continue
            
            crews.append(member)  # Ajouter le membre à l'équipage au sol

        # Charger les vaisseaux et leurs équipages
        for spaceship_data in data.get("spaceships", []):
            spaceship = Spaceship(
                spaceship_data["name"],
                spaceship_data["ship_type"],
                spaceship_data["condition"]
            )
            
            # Charger les membres d'équipage pour chaque vaisseau
            for member_data in spaceship_data.get("crew", []):
                role = member_data.get("role") or member_data.get("Rôle")

                if role == "civil":
                    member = Person(
                        member_data["first_name"],
                        member_data["last_name"],
                        member_data["gender"],
                        member_data["age"]
                    )
                elif role == "pilote" or role == "technicien":
                    member = Operator(
                        member_data["first_name"],
                        member_data["last_name"],
                        member_data["gender"],
                        member_data["age"],
                        role
                    )
                elif role == "mentalist":
                    member = Mentalist(
                        member_data["first_name"],
                        member_data["last_name"],
                        member_data["gender"],
                        member_data["age"]
                    )
                else:
                    print(f"Rôle inconnu : {role}. Impossible de charger ce membre.")
                    continue
                
                spaceship.add_member(member)  
                
            fleet.add_spaceship(spaceship) 

        print("Données chargées avec succès.")
        return fleet, crews  

    except FileNotFoundError:
        print(f"Aucun fichier trouvé avec le nom {file_name}.")
        return Fleet("Flotte Alpha"), []

def main():
    fleet, crews = load_data()  

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
        print("9. Supprimer un membre de l'équipage")
        print("0. Quitter")
        
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
                remove_choice = input("Supprimer un membre de l'équipage au sol (1) ou d'un vaisseau (2) ? ")
                if remove_choice == "1":
                    display_crew()
                    remove_member(crews)  
                elif remove_choice == "2":
                    display_spaceships(fleet) 
                    spaceship_choice = int(input("Choisissez un vaisseau (numéro) : ")) - 1
                    spaceship = fleet.spaceships[spaceship_choice]
                    remove_member(spaceship.crew) 
                else:
                    print("Option invalide.")
            case "0":
                save_data(fleet, crews)
                print("Au revoir!")
                break
            case _:
                print("Option invalide.")

if __name__ == "__main__":
    main()
