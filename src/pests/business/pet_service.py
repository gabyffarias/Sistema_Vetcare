from fastapi import HTTPException

class PetService:

    def __init__(self, pet_repo, tutor_repo):
        self.pet_repo = pet_repo
        self.tutor_repo = tutor_repo

    def cadastrar_pet(self, nome: str, especie: str, raca: str, idade: int, tutor_id: int):
        tutores = self.tutor_repo.listar_todos()
        tutor_existe = any(t["id"] == tutor_id for t in tutores)
        
        if not tutor_existe:
            raise HTTPException(
                status_code= 404,
                detail= "Tutor não encontrado. Não é possível cadastrar um pet para um tutor inexistente."  
            )
        pet_data = {
            "nome": nome,
            "especie": especie,
            "raca": raca,
            "idade": idade,
            "tutor_id": tutor_id
        }
        return self.pet_repo.salvar(pet_data)

    def listar_pets(self):
        return self.pet_repo.listar_todos()