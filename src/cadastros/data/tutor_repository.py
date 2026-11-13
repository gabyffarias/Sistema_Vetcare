from typing import List, Optional

class TutorRepository:
    
    def __init__(self):
        self._tutores= []
        self._proximo_id= 1

    def salvar(self, tutor_dados: dict) -> dict:

        tutor_dados["id"] = self._proximo_id
        self._tutores.append(tutor_dados)
        self._proximo_id += 1
        return tutor_dados

    def listar_todos(self) -> List[dict]:
        return self._tutores

    def buscar_por_cpf(self, cpf: str) -> Optional[dict]:

        for tutor in self._tutores:
            if tutor["cpf"] == cpf:
                return tutor

        return None