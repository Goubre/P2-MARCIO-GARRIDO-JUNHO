class AnimalDTO:

    def __init__(self, animal):
        self.id = animal.id
        self.nome = animal.nome
        self.cidade = animal.cidade
        self.status = animal.status

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cidade": self.cidade,
            "status": self.status
        }