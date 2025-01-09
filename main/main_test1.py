from Person import Person  # Importation de la classe Person
from Operator import Operator  # Importation de la classe Operator
from Mentalist import Mentalist  # Importation de la classe Mentalist
from Spaceship import Spaceship  # Importation de la classe Spaceship
from Fleet import Fleet  # Importation de la classe Fleet
import crew  # Importation des fonctions de gestion de l'équipage

# Fonction principale qui lance le menu
def main():
    fleet = Fleet("Flotte Alpha")
    spaceship1 = Spaceship("Apollo", "Transport", "Opérationnel")
    spaceship2 = Spaceship("Orion", "Guerre", "Endommagé")

    # Ajouter des vaisseaux à la flotte
    fleet.add_spaceship(spaceship1)
    fleet.add_spaceship(spaceship2)

    # Lancer le menu
    crew.menu()

if __name__ == "__main__":
    main()
