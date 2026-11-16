from src.cadastros.data.tutor_repository import TutorRepository
from fastapi import HTTPException

class TutorService:

    def __init__(self,repository: TutorRepository):
        self.repository = repository

    def cadastrar_tutor(self, nome: str, cpf: str, telefone: str, email: str) -> dict:

        tutor_existente= self.repository.buscar_por_cpf(cpf)
        if tutor_existente:
            raise ValueError("Já existe um tutor cadastrado com este CPF.")

        novo_tutor= {
            "nome": nome,
            "cpf": cpf,
            "telefone": telefone,
            "email": email
        }
        return self.repository.salvar(novo_tutor)
    
    def listar_tutores(self) -> list:
        return self.repository.listar_todos()

    def atualizar_tutor(self, tutor_id: int, nome: str, telefone: str, email: str):
        dados = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }
        tutor_atualizado = self.repository.atualizar(tutor_id, dados)
        if not tutor_atualizado:
            raise HTTPException(status_code=404, detail="Tutor não encontrado para atualização.")
        return tutor_atualizado

    def deletar_tutor(self, tutor_id: int):
        sucesso = self.repository.deletar(tutor_id)
        if not sucesso:
            raise HTTPException(status_code=404, detail="Tutor não encontrado para exclusão.")
        return {"mensagem": "Tutor removido com sucesso."}