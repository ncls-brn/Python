from Person import Person  # Importation de la classe Person
from Operator import Operator  # Importation de la classe Operator
from Mentalist import Mentalist  # Importation de la classe Mentalist
from Spaceship import Spaceship  # Importation de la classe Spaceship
from Fleet import Fleet  # Importation de la classe Fleet

# --- TEST DES CLASSES PERSON ET OPERATOR ---

# Création de plusieurs objets Person
person1 = Person("John", "Doe", "M", 30)
person2 = Person("Alice", "Smith", "F", 28)
person3 = Person("Bob", "Brown", "M", 35)

# Test de l'instanciation et des méthodes de la classe Person
print(person1.introduce_yourself())
print(person2.introduce_yourself())
print(person3.introduce_yourself())

# Création de plusieurs objets Operator
operator1 = Operator("Charlie", "Johnson", "M", 40, "Pilote", 5)
operator2 = Operator("Carla", "Green", "F", 32, "Technicien", 3)

# Test des méthodes de la classe Operator
print(f"{operator1.get_first_name()} {operator1.get_last_name()} : {operator1.get_role()}")
operator1.act()

print(f"{operator2.get_first_name()} {operator2.get_last_name()} : {operator2.get_role()}")
operator2.act()
operator2.gain_experience()

# --- TEST DE LA CLASSE MENTALIST ---

# Création d'un objet Mentalist
mentalist1 = Mentalist("Gaal", "Dornick", "M", 40, 100)

# Test des méthodes de la classe Mentalist
print(f"{mentalist1.get_first_name()} {mentalist1.get_last_name()} a {mentalist1.get_mana()} points de mana.")
mentalist1.recharge_mana()

# Création d'un autre objet Mentalist
mentalist2 = Mentalist("Salvor", "Hardin", "F", 30, 50)
mentalist2.act(operator1)  # Le mentaliste influence un opérateur

# --- TEST DE LA CLASSE SPACESHIP ---

# Création d'un vaisseau
spaceship1 = Spaceship("Apollo", "Transport", "Opérationnel")
spaceship2 = Spaceship("Orion", "Guerre", "Endommagé")

# Ajouter des membres à l'équipage
spaceship1.add_member(operator1)
spaceship1.add_member(person1)
spaceship1.add_member(mentalist1)
spaceship2.add_member(person2)
spaceship2.add_member(operator2)

# Vérification de la préparation des vaisseaux
print(f"Le vaisseau {spaceship1.name} est prêt pour la mission: {spaceship1.check_preparation()}")
print(f"Le vaisseau {spaceship2.name} est prêt pour la mission: {spaceship2.check_preparation()}")

# --- TEST DE LA CLASSE FLEET ---

# Création d'une flotte
fleet = Fleet("Flotte Alpha")

# Ajouter des vaisseaux à la flotte
fleet.add_spaceship(spaceship1)
fleet.add_spaceship(spaceship2)

# Afficher les statistiques de la flotte
fleet.statistics()

# --- AFFICHAGE DES INFORMATIONS ---

# Affichage des informations de tous les vaisseaux dans la flotte
print("\nInformations sur les vaisseaux de la flotte :")
for spaceship in fleet.spaceships:
    spaceship.display_info()
