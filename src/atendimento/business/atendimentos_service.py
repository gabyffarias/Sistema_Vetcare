from fastapi import HTTPException

class AtendimentoService:

    def __init__(self, atendimento_repo, pet_repo):
        self.atendimento_repo= atendimento_repo
        self.pet_repo= pet_repo

    def registrar_atendimento(self, pet_id: int, data_consulta: str, motivo: str, diagnostico: str, valor: float):

        pets= self.pet_repo.listar_todos()
        pet_existe= any(p["id"] == pet_id for p in pets)

        if not pet_existe:
            raise HTTPException(
                status_code= 404,
                detail= "Pet não encontrado. Não é possível atendimento para um animal inexistente."
            )

        atendimento_data= {
            "pet_id": pet_id,
            "data_consulta": data_consulta,
            "motivo": motivo,
            "diagnostico": diagnostico,
            "valor": valor
        }
        return self.atendimento_repo.salvar(atendimento_data)

    def listar_atendimentos(self):
        return self.atendimento_repo.listar_todos()