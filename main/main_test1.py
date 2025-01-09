from Person import Person  # Importation de la classe Person
from Operator import Operator  # Importation de la classe Operator
from Mentalist import Mentalist  # Importation de la classe Mentalist
from Spaceship import Spaceship  # Importation de la classe Spaceship
from Fleet import Fleet  # Importation de la classe Fleet

def add_member(fleet):
    # Créer un membre
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
        return None

    # Choisir le vaisseau auquel assigner le membre
    print("\nChoisissez le vaisseau auquel ajouter ce membre :")
    fleet.display_fleet()
    spaceship_choice = int(input("Entrez le numéro du vaisseau : "))
    spaceship = fleet.get_spaceship(spaceship_choice)
    
    if spaceship:
        spaceship.add_member(new_member)  # Assigner le membre au vaisseau
    return new_member

def create_spaceship():
    name = input("Entrez le nom du vaisseau : ")
    type = input("Entrez le type du vaisseau (transport, guerre, etc.) : ")
    condition = input("Entrez l'état du vaisseau (opérationnel, endommagé) : ")
    return Spaceship(name, type, condition)

def add_spaceship_to_fleet(fleet):
    spaceship = create_spaceship()
    fleet.add_spaceship(spaceship)
    print(f"Le vaisseau {spaceship.name} a été ajouté à la flotte {fleet.name}.")

def menu():
    fleet = Fleet("Flotte Alpha")
    spaceship1 = Spaceship("Apollo", "Transport", "Opérationnel")
    spaceship2 = Spaceship("Orion", "Guerre", "Endommagé")

    fleet.add_spaceship(spaceship1)
    fleet.add_spaceship(spaceship2)

    while True:
        print("\nMENU :")
        print("1. Ajouter un membre d'équipage à un vaisseau")
        print("2. Créer un vaisseau")
        print("3. Ajouter un vaisseau à une flotte")
        print("4. Afficher les vaisseaux de la flotte")
        print("5. Quitter le menu")

        choice = int(input("Choisissez l'option souhaitée : "))

        match choice:
            case 1:
                add_member(fleet)  # Ajouter un membre à un vaisseau dans la flotte
            case 2:
                add_spaceship_to_fleet(fleet)  # Créer un nouveau vaisseau et l'ajouter à la flotte
            case 3:
                add_spaceship_to_fleet(fleet)  # Ajouter un vaisseau à la flotte
            case 4:
                fleet.display_fleet()  # Afficher tous les vaisseaux de la flotte
                spaceship_choice = int(input("Choisissez le vaisseau à afficher (entrez le numéro) : "))
                spaceship = fleet.get_spaceship(spaceship_choice)  # Obtenir le vaisseau choisi
                if spaceship:
                    spaceship.display_info()  # Afficher les informations du vaisseau et son équipage
            case 5:
                print("Quitter le menu.")
                break
            case _:
                print("Le choix sélectionné n'existe pas.")

if __name__ == "__main__":
    menu()
