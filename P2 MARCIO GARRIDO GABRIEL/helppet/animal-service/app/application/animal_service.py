from app.domain.animal_factory import AnimalFactory
from app.infrastructure.animal_repository import AnimalRepository


class AnimalService:

    def __init__(self):
        self.repository = AnimalRepository()

    def list_animals(self):
        return self.repository.get_all()

    def create_animal(self, nome, cidade):

        animal = AnimalFactory.create(
            len(self.repository.get_all()) + 1,
            nome,
            cidade
        )

        self.repository.add(animal)

        return animal

    def mark_as_found(self, animal_id):

        animal = self.repository.find_by_id(animal_id)

        if animal:
            animal.status = "Encontrado"
            return animal

        return None