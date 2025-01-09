class Person:
    
    def __init__(self, first_name, last_name, gender, age, role="Membre"):
        self.__first_name = first_name  
        self.__last_name = last_name  
        self.__gender = gender  
        self.__age = age
        self.__role = role  # Ajout de l'attribut role
    
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def get_role(self):
        return self.__role

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_gender(self, gender):
        self.__gender = gender

    def set_age(self, age):
        if age >= 0: 
            self.__age = age
        else:
            print("L'âge ne peut pas être négatif.")
    
    def introduce_yourself(self):
        return f"Bonjour, mon nom est {self.__first_name} {self.__last_name}. J'ai {self.__age} ans et je suis {self.__gender}."
