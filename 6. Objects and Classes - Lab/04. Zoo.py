class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammals':
            self.mammals.append(name)
        elif species == 'fishes':
            self.fishes.append(name)
        elif species == 'birds':
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        zoo_name = self.name
        if species == 'mammals':
            species_name = self.mammals
        if species == 'fishes':
            species_name = self.fishes
        if species == 'birds':
            species_name = self.birds
        names = ', '.join(zoo_name)
        return f"{species} in {zoo_name}: {names}"

    def get_total(self):
        return f'Total animals: {self.__animals}'


zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())
for _ in range(n):
    species, name = input().split(' ')
    zoo.add_animal(species, name)
species = input()
print(zoo.get_info(species))
print(zoo.get_total())
