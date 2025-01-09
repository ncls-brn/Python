class Spaceship:
    def __init__(self, name, type, condition):
        self.name = name  # Nom du vaisseau
        self.type = type  # Type du vaisseau (ex : "transport", "guerre", "marchand")
        self.condition = condition  # Condition du vaisseau (ex : "opérationnel", "endommagé")
        self.crew = []  # Liste d'équipage du vaisseau

    def add_member(self, member):
        self.crew.append(member)
        print(f"{member.get_first_name()} {member.get_last_name()} a été ajouté à l'équipage du vaisseau {self.name}.")

    def display_info(self):
        print(f"\nVaisseau {self.name} :")
        print(f"Type : {self.type}")
        print(f"État : {self.condition}")
        print(f"Équipage ({len(self.crew)} membres) :")
        for member in self.crew:
            print(f"- {member.get_first_name()} {member.get_last_name()} ({member.get_role()})")
