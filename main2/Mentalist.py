from Person import Person

class Mentalist(Person):
    def __init__(self, first_name, last_name, gender, age, mana=100):
        super().__init__(first_name, last_name, gender, age)
        self.mana = mana

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age 
    
    def get_mana(self):
        return self.mana
    
    def act(self, target):
        if self.mana >= 20:
            self.mana -= 20
            print(f"{self.first_name} utilise son pouvoir mental sur {target.first_name}.")
        else:
            print("Pas assez de mana pour influencer.")

    def recharge_mana(self):
        if self.mana < 100:
            self.mana += 50
            print(f"{self.first_name} recharge son mana.")


class Mentalist(Person):
    def __init__(self, first_name, last_name, gender, age, mana=100):
        super().__init__(first_name, last_name, gender, age)
        self.mana = mana

    def act(self, target):
        if self.mana >= 20:
            self.mana -= 20
            print(f"{self.first_name} utilise son pouvoir mental sur {target.first_name}.")
        else:
            print("Pas assez de mana pour influencer.")

    def recharge_mana(self):
        if self.mana < 100:
            self.mana += 50
            print(f"{self.first_name} recharge son mana.")
