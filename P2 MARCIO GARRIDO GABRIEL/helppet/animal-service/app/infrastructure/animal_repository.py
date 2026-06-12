from app.domain.animal import Animal


class AnimalRepository:

    def __init__(self):
        self.animals = [
            Animal(
                1,
                "Rex",
                "Maricá",
                "Perdido"
            )
        ]

    def get_all(self):
        return self.animals

    def add(self, animal):
        self.animals.append(animal)

    def find_by_id(self, animal_id):

        for animal in self.animals:

            if animal.id == animal_id:
                return animal

        return None