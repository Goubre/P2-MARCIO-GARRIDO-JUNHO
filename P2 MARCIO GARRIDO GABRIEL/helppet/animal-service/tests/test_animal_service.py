from app.application.animal_service import AnimalService


def test_create_animal():

    service = AnimalService()

    animal = service.create_animal(
        "Bolt",
        "Maricá"
    )

    assert animal.nome == "Bolt"
    assert animal.cidade == "Maricá"
    assert animal.status == "Perdido"