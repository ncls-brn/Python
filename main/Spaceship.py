from Person import Person  # Assurez-vous que la classe Person est importée

class Spaceship:
    def __init__(self, name, type, condition):
        self.name = name  # Nom du vaisseau
        self.type = type  # Type du vaisseau (ex : "transport", "guerre", "marchand")
        self.crew = []  # Liste vide pour l'équipage
        self.condition = condition  # Condition du vaisseau (ex : "opérationnel", "endommagé")

    # Méthode pour ajouter un membre à l'équipage
    def add_member(self, person):
        if len(self.crew) < 10:
            self.crew.append(person)
            print(f"{person.get_first_name()} {person.get_last_name()} a été ajouté à l'équipage du vaisseau {self.name}.")
        else:
            print(f"Capacité maximale de 10 membres atteinte pour le vaisseau {self.name}. Impossible d'ajouter {person.get_first_name()} {person.get_last_name()}.")

    # Méthode pour vérifier si le vaisseau est prêt à partir
    def check_preparation(self):
        has_pilot = False
        has_technician = False

        for member in self.crew:
            if member.get_role().lower() == "pilote":
                has_pilot = True
            elif member.get_role().lower() == "technicien":
                has_technician = True

            # Si un pilote et un technicien sont présents, on peut partir en mission
            if has_pilot and has_technician:
                return True
        return False

    # Méthode pour afficher les informations du vaisseau et de son équipage
    def display_info(self):
        print(f"Nom du vaisseau : {self.name}")
        print(f"Type du vaisseau : {self.type}")
        print(f"État du vaisseau : {self.condition}")
        print(f"Équipage ({len(self.crew)} membres) :")
        for member in self.crew:
            print(f"- {member.get_first_name()} {member.get_last_name()} ({member.get_role()})")
