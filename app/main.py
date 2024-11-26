class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def remove_from_alive(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def check(self) -> None:
        if self.health <= 0:
            self.remove_from_alive()

    def __repr__(self) -> str:
        return f'{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}'


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: "Herbivore") -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            other.check()
