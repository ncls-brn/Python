from Person import Person

class Mentalist(Person):
    def __init__(self, first_name, last_name, gender, age, mana=100):
        super().__init__(first_name, last_name, gender, age)
        self.__mana = mana  
    
    
    def get_mana(self):
        return self.__mana

    def set_mana(self, mana):
        if 0 <= mana <= 100:
            self.__mana = mana
        else:
            print("Les points de mana doivent être compris entre 0 et 100.")
    
    
    def act(self, target_person):
        if self.get_mana() >= 20:
            self.__mana -= 20
            print(f"{self.get_first_name()} {self.get_last_name()} utilise son pouvoir mental pour influencer {target_person.get_first_name()} {target_person.get_last_name()}.")
            target_person.act()
        else:
            print(f"{self.get_first_name()} {self.get_last_name()} n'a pas assez de mana pour agir.")
    
    
    def recharge_mana(self):
        if self.get_mana() < 100:
            self.__mana = min(self.get_mana() + 50, 100)
            print(f"{self.get_first_name()} {self.get_last_name()} recharge son mana. Mana actuel: {self.get_mana()}")
        else:
            print(f"{self.get_first_name()} {self.get_last_name()} a déjà un mana complet.")
