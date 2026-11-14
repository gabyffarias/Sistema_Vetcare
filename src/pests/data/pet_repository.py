class PetRepository:

    def __init__(self):
        self.pets= []
        self._id= 1 

    def salvar(self, pet_data: dict) -> dict:
        novo_pet= {
            "id": self._id,
            "nome": pet_data["nome"],
            "especie": pet_data["especie"],
            "raca": pet_data.get("raca"),
            "idade": pet_data["idade"],
            "tutor_id": pet_data["tutor_id"]
        }
        self.pets.append(novo_pet)
        self._id += 1
        return novo_pet

    def listar_todos(self) -> list:
        return self.pets