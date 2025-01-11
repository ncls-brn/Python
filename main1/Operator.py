from Person import Person

class Operator(Person):
    def __init__(self, first_name, last_name, gender, age, role, experience=1):
        super().__init__(first_name, last_name, gender, age)
        self.role = role
        self.experience = experience

    def get_role(self):
        return self.role
    
    def get_experience(self):
        return self.experience
    
    def to_dict(self):
        data = super().to_dict()
        data["Rôle"] = self.role
        return data
    
    def act(self):
        print(f"{self.first_name} {self.last_name} est en action en tant que {self.role}.")

    def gain_experience(self):
        self.experience += 3
        print(f"{self.first_name} {self.last_name} a gagné 3 point d'expérience.")

