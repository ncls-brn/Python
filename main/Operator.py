from Person import Person

class Operator(Person):
    def __init__(self, first_name, last_name, gender, age, role, experience=0):
        super().__init__(first_name, last_name, gender, age)
        
        self.__role = role 
        self.__experience = experience  

    # Getters et Setters pour le rôle et l'expérience
    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = role

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        if experience >= 0:  
            self.__experience = experience
        else:
            print("L'expérience ne peut pas être négative.")

    # Fonction act() qui utilise les getters
    def act(self):
        if self.get_role().lower() == "technicien":
            print(f"{self.get_first_name()} {self.get_last_name()} est en train de réparer l'équipement.")
        elif self.get_role().lower() == "pilote":
            print(f"{self.get_first_name()} {self.get_last_name()} est en train de piloter le vaisseau.")
        elif self.get_role().lower() == "navigateur":
            print(f"{self.get_first_name()} {self.get_last_name()} est en train de naviguer dans la galaxie.")
        else:
            print(f"{self.get_first_name()} {self.get_last_name()} est en train de faire une tâche monotone.")
    
    # Gain d'expérience
    def gain_experience(self):
        self.__experience += 1
        print(f"{self.get_first_name()} {self.get_last_name()} a maintenant {self.get_experience()} années d'XP.")
