from fastapi import APIRouter, status
from pydantic import BaseModel, Field
from src.atendimento.data.atendimentos_repository import AtendimentoRepository
from src.atendimento.business.atendimentos_service import AtendimentoService
from src.pests.presentation.pets_routes import pet_repo

router= APIRouter(prefix= "/atendimento", tags= ["Atendimento"])

atendimento_repo= AtendimentoRepository()
atendimento_service= AtendimentoService(atendimento_repo, pet_repo)

class AtendimentoCreateRequest(BaseModel):
    pet_id: int = Field(..., description= "ID do pet atendido")
    data_consulta: str = Field(..., min_legth=8, description= "Data da consulta no modelo: 00/00/0000 .")
    motivo: str = Field(..., min_legth=3, description= "Motivo da consulta (EX: vacinação, Check-up).")
    diagnostico: str = Field(None, decription= "Diagnóstico ou observação do veterinário.")
    valor: int = Field(..., gt= 0,secription= "Valor do atendimento em reais (deve ser maior que 0.)")

@router.post("", status_code=status.HTTP_201_CREATED)

def criar_atendimento(dados: AtendimentoCreateRequest):

    return atendimento_service.registrar_atendimento(
        pet_id= dados.pet_id,
        data_consulta= dados.data_consulta,
        motivo= dados.motivo,
        diagnostico= dados.diagnostico,
        valor= dados.valor
    )

@router.get("", status_code=status.HTTP_200_OK)

def listar_atendimento():
    return atendimento_service.listar_atendimentos()

@router.put("/{atendimento_id}", status_code=status.HTTP_200_OK)

def atualizar_atendimento(atendimento_id: int, dados: AtendimentoCreateRequest):
    return atendimento_service.atualizar_atendimento(
        atendimento_id=atendimento_id,
        pet_id=dados.pet_id,
        data_consulta=dados.data_consulta,
        motivo=dados.motivo,
        diagnostico=dados.diagnostico,
        valor=dados.valor
    )

@router.delete("/{atendimento_id}", status_code=status.HTTP_200_OK)

def deletar_atendimento(atendimento_id: int):
    return atendimento_service.deletar_atendimento(atendimento_id)