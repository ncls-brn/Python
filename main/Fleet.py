from Operator import Operator
from Mentalist import Mentalist


class Fleet:
    def __init__(self, name):
        self.name = name
        self.spaceships = []

    def add_spaceship(self, spaceship):
        if len(self.spaceships) < 15:  # Capacité maximale de 15 vaisseaux par flotte
            self.spaceships.append(spaceship)
            print(f"Le vaisseau {spaceship.name} a été ajouté à la flotte {self.name}.")
        else:
            print("La flotte a atteint sa capacité maximale de vaisseaux.")

    def statistics(self):
        print(f"\nStatistiques de la flotte {self.name}:")
        total_members = 0
        role_distribution = {"pilote": 0, "technicien": 0, "mentaliste": 0}
        for spaceship in self.spaceships:
            total_members += len(spaceship.crew)
            for member in spaceship.crew:
                if isinstance(member, Operator):
                    role_distribution[member.role] += 1
                elif isinstance(member, Mentalist):
                    role_distribution["mentaliste"] += 1

        print(f"Nombre total de membres dans la flotte : {total_members}")
        print(f"Répartition par rôle : Pilotes - {role_distribution['pilote']}, Techniciens - {role_distribution['technicien']}, Mentalistes - {role_distribution['mentaliste']}")
