from Person import Person

class Operator(Person):
    def __init__(self, first_name, last_name, gender, age, role, experience=0):
        super().__init__(first_name, last_name, gender, age)
        self.__role = role
        self.__experience = experience

    def get_role(self):
        return self.__role
    
    def to_dict(self):
        data = super().to_dict()
        data["role"] = self.__role
        return data
    
    def act(self):
        print(f"{self.__first_name} {self.__last_name} est en action en tant que {self.__role}.")

    def gain_experience(self):
        self.__experience += 1
        print(f"{self.__first_name} {self.__last_name} a gagné 1 point d'expérience.")

