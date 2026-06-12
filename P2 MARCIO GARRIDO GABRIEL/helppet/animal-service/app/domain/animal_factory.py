from app.domain.animal import Animal


class AnimalFactory:

    @staticmethod
    def create(id, nome, cidade):

        return Animal(
            id,
            nome,
            cidade,
            "Perdido"
        )