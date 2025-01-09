class Fleet:
    def __init__(self, name):
        self.name = name
        self.spaceships = []  # Liste pour stocker les vaisseaux

    def add_spaceship(self, spaceship):
        self.spaceships.append(spaceship)
        print(f"Le vaisseau {spaceship.name} a été ajouté à la flotte {self.name}.")

    def display_fleet(self):
        if not self.spaceships:
            print("La flotte est vide.")
            return
        
        print(f"\nFlotte {self.name} :")
        for i, spaceship in enumerate(self.spaceships, 1):
            print(f"{i}. {spaceship.name}")  # Afficher les vaisseaux avec leur numéro

    def get_spaceship(self, choice):
        if 1 <= choice <= len(self.spaceships):
            return self.spaceships[choice - 1]  # Retourner le vaisseau choisi
        else:
            print("Choix invalide.")
            return None
