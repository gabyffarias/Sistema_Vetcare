class AtendimentoRepository:

    def __init__(self):
        self.atendimento= []
        self._id= 1

    def salvar(self, atendimento_data: dict) -> dict:

        novo_atendimento= {
            "id": self._id,
            "pet_id": atendimento_data["pet_id"],
            "data_consulta": atendimento_data["data_consulta"],
            "motivo": atendimento_data["motivo"],
            "diagnostico": atendimento_data.get("diagnostico", "Em avaliação"),
            "valor": atendimento_data["valor"]
        }
        self.atendimento.append(novo_atendimento)
        self._id += 1
        return novo_atendimento

    def listar_todos(self) -> list:
        return self.atendimento

    def buscar_por_id(self, atendimento_id: int) -> dict | None:
        
        for atendimento in self.atendimento:
            if atendimento["id"] == atendimento_id:
                return atendimento
        
        return None

    def atualizar(self, atendimento_id: int, dados_atualizados: dict) -> dict | None:
        
        atendimento = self.buscar_por_id(atendimento_id)
        if atendimento:
            atendimento.update(dados_atualizados)
            return atendimento
        
        return None

    def deletar(self, atendimento_id: int) -> bool:
        
        atendimento = self.buscar_por_id(atendimento_id)
        if atendimento:
            self.atendimento.remove(atendimento)
            return True
        
        return False