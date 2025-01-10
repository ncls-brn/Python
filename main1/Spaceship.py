from Operator import Operator
from Mentalist import Mentalist

class Spaceship:
    def __init__(self, name, ship_type, condition="opérationnel"):
        self.name = name
        self.ship_type = ship_type
        self.condition = condition
        self.crew = []

    def add_member(self, member):
        if len(self.crew) < 10:  # Capacité maximale de 10 membres par vaisseau
            self.crew.append(member)
            print(f"{member.first_name} {member.last_name} ajouté à l'équipage du vaisseau {self.name}.")
        else:
            print(f"Le vaisseau {self.name} a atteint sa capacité maximale d'équipage.")

    def check_preparation(self):
        pilots = [m for m in self.crew if isinstance(m, Operator) and m.role == "pilote"]
        technicians = [m for m in self.crew if isinstance(m, Operator) and m.role == "technicien"]
        mentalists = [m for m in self.crew if isinstance(m, Mentalist) and m.mana >= 50]

        if pilots and technicians and mentalists:
            print(f"Le vaisseau {self.name} est prêt pour la mission.")
            return True
        else:
            print(f"Le vaisseau {self.name} n'est pas prêt. Il manque des membres essentiels.")
            return False

    def display_crew_details(self):
        if not self.crew:
            print(f"L'équipage du vaisseau {self.name} est vide.")
            return
        
        print(f"Détails de l'équipage du vaisseau {self.name} :")
        for member in self.crew:
            print(f"Nom : {member.first_name} {member.last_name}")
            print(f"Genre : {member.gender}")
            print(f"Âge : {member.age} ans")
            if isinstance(member, Operator):
                print(f"Rôle : {member.role}")
            elif isinstance(member, Mentalist):
                print(f"Mana : {member.mana}")
            print("-----------------------------")