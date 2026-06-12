from fastapi import APIRouter
from app.application.animal_service import AnimalService
from app.domain.animal_dto import AnimalDTO

router = APIRouter()

animal_service = AnimalService()


@router.get("/animals")
def list_animals():
    animals = animal_service.list_animals()

    return [
        AnimalDTO(animal).to_dict()
        for animal in animals
    ]


@router.post("/animals")
def create_animal(nome: str, cidade: str):
    animal = animal_service.create_animal(nome, cidade)

    return AnimalDTO(animal).to_dict()


@router.put("/animals/{animal_id}/found")
def mark_animal_as_found(animal_id: int):
    animal = animal_service.mark_as_found(animal_id)

    if animal is None:
        return {"error": "Animal não encontrado"}

    return AnimalDTO(animal).to_dict()