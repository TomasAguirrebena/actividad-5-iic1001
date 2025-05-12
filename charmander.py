from abc import ABC
import time as t

# clase abstracta de pokemon
class Pokemon(ABC):

    def __init__(self, name, level, type_):
        self.name = name
        self.level = level
        self.hp = 100
        self.max_hp = 100
        self.type_ = type_
    
    # propiedad que maneja la vida de nuestro pokemon
    @property
    def hp(self):
        return self._hp
    def hp(self, value):
        if value < 0:
            self._hp = 0
        elif value > self.max_hp:
            self._hp = self.max_hp
        else:
            self._hp = value

    def attack(self):
        pass

    def __str__(self):
        return f'{self.name} (nivel {self.level}) - tipo: {self.type_} - HP: {self.hp}/{self.max_hp}'

    def yell(self):
        print(f"{self.name}!")

# charmander!!! char char!!!
class Charmander(Pokemon):

    def __init__(self, name, level):
        super().__init__(name, level, "Fire")
        self.type_ = "Fire"
        self.hp = 100
        self.max_hp = 100
        self.level = level
        self.name = name
    
    def attack(self):
        return f"{self.name} uso Flamethrower!"
    
    def speak(self):
        print(f"Char! Char!")

char = Charmander("Charmander", 31)
char.speak()

# lo copie y pege mucho trabajo hacerlo desde 0
print("Jessie: ¡Prepárense para los problemas!")
print("James: ¡Y más vale que teman!")
print("Jessie: Para proteger al mundo de la devastación.")
print("James: Para unir a los pueblos dentro de nuestra nación.")
print("Jessie: Para denunciar los males de la verdad y el amor.")
print("James: Para extender nuestro reino hasta las estrellas.")
print("Jessie: ¡Jessie!")
print("James: ¡Jame-me-me-mes!")
print("Jessie: ¡El Equipo Rocket viajando a la velocidad de la luz!")
print("James: ¡Ríndanse ahora o prepárense a luchar!")
print("Meowth: ¡Meowth! ¡Así es!")

char.yell()
print(char.attack())

print("el equipo rocket a sido vencidoooooo otra vez !!!!")