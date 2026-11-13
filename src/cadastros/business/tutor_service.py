from src.cadastros.data.tutor_repository import TutorRepository

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