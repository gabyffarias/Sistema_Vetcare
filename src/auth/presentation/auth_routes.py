from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router= APIRouter()

class LoginRequest(BaseModel):
    email: str
    senha: str

@router.post("/login")
def fazer_login(dados: LoginRequest):

    if dados.email == "admin@vetcare.com" and dados.senha == "123456":
        return {
            "mensagem": "Login realizado com sucesso!",
            "usuário": dados.email,
            "perfil": "Administrador"
        }

    raise HTTPException(status_code=401, detail="E-mail ou senha inv")