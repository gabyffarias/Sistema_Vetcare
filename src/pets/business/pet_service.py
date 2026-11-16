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

    def atualizar_pet(self, pet_id: int, tutor_id: int, nome: str, especie: str, raca: str):
       
        tutor = self.tutor_repo.buscar_por_id(tutor_id)
        if not tutor:
            raise HTTPException(status_code=404, detail="Tutor não encontrado para vincular ao pet.")

        dados = {
            "tutor_id": tutor_id,
            "nome": nome,
            "especie": especie,
            "raca": raca
        }
        pet_atualizado = self.pet_repo.atualizar(pet_id, dados)
        if not pet_atualizado:
            raise HTTPException(status_code=404, detail="Pet não encontrado para atualização.")
        
        return pet_atualizado

    def deletar_pet(self, pet_id: int):
        
        sucesso = self.pet_repo.deletar(pet_id)
        if not sucesso:
            raise HTTPException(status_code=404, detail="Pet não encontrado para exclusão.")
        
        return {"mensagem": "Pet removido com sucesso."}