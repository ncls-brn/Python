class Person:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age    

    def introduce_yourself(self):
        return f"Je m'appelle {self.first_name} {self.last_name}, je suis un(e) {self.gender} de {self.age} ans."
