from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, EmailStr, field_validator
import re
from src.cadastros.data.tutor_repository import TutorRepository
from src.cadastros.business.tutor_service import TutorService

router= APIRouter()

tutor_repo= TutorRepository()
tutor_service= TutorService(tutor_repo)

class TutorCreateRequest(BaseModel):

    nome: str = Field(..., min_length=3, description= "Nome completo do tutor.")
    cpf: str = Field(..., min_length=11, max_lengt=14, description= "CPF do tutor.")
    telefone: str = Field(...,min_length=8, description= "Telefone de contato.")
    email: str = Field(..., description= "Email do tutor.")

    @field_validator('cpf')
    @classmethod

    def validar_cpf_digitos(cls, v:str) -> str:

        apenas_numeros= re.sub(r'\D', '', v)
        
        if len(apenas_numeros) != 11:
            raise ValueError("O CPF deve conter exatamente 11 dígitos numéricos.")
        return apenas_numeros

@router.post("/tutores", status_code=201)
def criar_tutor(dados: TutorCreateRequest):

    try:
        tutor_criado = tutor_service.cadastrar_tutor(
            nome= dados.nome,
            cpf= dados.cpf,
            telefone= dados.telefone,
            email= dados.email
        )
        return {"mensagem": "Tutor cadstrado com sucesso!", "tutor": tutor_criado}
    except ValueError as e:
        raise HTTPException(status_code=400, detail= str(e))

@router.get("/tutores")
def listar_tutores():
    return tutor_service.listar_tutores()