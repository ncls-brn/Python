from Person import Person

class Mentalist(Person):
    def __init__(self, first_name, last_name, gender, age, mana=10):
        super().__init__(first_name, last_name, gender, age)
        self.mana = mana

    def to_dict(self):
        data = super().to_dict()
        data["mana"] = self.mana
        return data
    
    def act(self, target):
        if self.mana >= 20:
            self.mana -= 20
            print(f"{self.first_name} utilise son pouvoir mental sur {target.first_name}.")
        else:
            print(f"{self.first_name} n'a pas assez de mana pour influencer {target.first_name}")

    def recharge_mana(self):
        if self.mana < 100:
            self.mana += 50
            print(f"{self.first_name} recharge son mana.")


