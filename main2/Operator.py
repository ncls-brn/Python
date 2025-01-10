from Person import Person

class Operator(Person):
    def __init__(self, first_name, last_name, gender, age, role, experience=0):
        super().__init__(first_name, last_name, gender, age)
        self.role = role
        self.experience = experience

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age 
    
    def get_role(self):
        return self.role
    
    def get_experience(self):
        return self.experience
    
    def act(self):
        print(f"{self.first_name} {self.last_name} est en action en tant que {self.role}.")

    def gain_experience(self):
        self.experience += 1
        print(f"{self.first_name} {self.last_name} a gagné 1 point d'expérience.")

