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

    def buscar_por_id(self, pet_id: int) -> dict | None:
        
        for pet in self.pets:
            if pet["id"] == pet_id:
                return pet
        
        return None

    def atualizar(self, pet_id: int, dados_atualizados: dict) -> dict | None:
        
        pet = self.buscar_por_id(pet_id)
        if pet:
            pet.update(dados_atualizados)
            return pet
        
        return None

    def deletar(self, pet_id: int) -> bool:
        
        pet = self.buscar_por_id(pet_id)
        if pet:
            self.pets.remove(pet)
            return True
        
        return False