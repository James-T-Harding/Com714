from human import Human


class Planet:
    def __init__(self, name: str):
        self.name = name
        self.humans = []

    def __repr__(self):
        return f"Planet(name = {self.name}, humans = {self.humans})"

    def __str__(self):
        return f"{self.name} contains {self.population()} humans."

    def add(self, human: Human):
        self.humans.append(human)

    def remove(self, human: Human):
        if ret := human in self.humans:
            self.humans.remove(human)

        return ret

    def has(self, human: Human):
        return human in self.humans

    def population(self):
        return len(self.humans)

