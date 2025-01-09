from Spaceship import Spaceship  # Assurez-vous que la classe Spaceship est importée
from Operator import Operator  # Assurez-vous que la classe Operator est importée

class Fleet:
    def __init__(self, name):
        self.name = name  # Nom de la flotte
        self.spaceships = []  # Liste vide pour les vaisseaux

    # Méthode pour ajouter un vaisseau à la flotte
    def add_spaceship(self, spaceship):
        if len(self.spaceships) < 15:
            self.spaceships.append(spaceship)
            print(f"Le vaisseau {spaceship.name} a été ajouté à la flotte {self.name}.")
        else:
            print(f"Capacité maximale de 15 vaisseaux atteinte pour la flotte {self.name}. Impossible d'ajouter {spaceship.name}.")

    # Méthode pour calculer les statistiques de la flotte
    def statistics(self):
        total_members = 0
        role_distribution = {}
        total_experience = 0
        operator_count = 0

        for spaceship in self.spaceships:
            for member in spaceship.crew:
                total_members += 1
                # Répartition des rôles
                role = member.get_role()
                if role in role_distribution:
                    role_distribution[role] += 1
                else:
                    role_distribution[role] = 1
                
                # Calcul de l'expérience des opérateurs
                if isinstance(member, Operator):
                    operator_count += 1
                    total_experience += member.get_experience()

        # Affichage des statistiques
        print(f"\nFlotte : {self.name}")
        print(f"Nombre total de membres dans la flotte : {total_members}")
        
        print("\nRépartition des rôles dans la flotte :")
        for role, count in role_distribution.items():
            print(f"{role}: {count} membres")
        
        # Niveau moyen d'expérience des opérateurs
        if operator_count > 0:
            average_experience = total_experience / operator_count
            print(f"\nNiveau moyen d'expérience des opérateurs : {average_experience:.2f}")
        else:
            print("\nAucun opérateur dans la flotte.")

