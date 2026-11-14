from fastapi import APIRouter, status
from pydantic import BaseModel, Field
from src.pests.data.pet_repository import PetRepository
from src.pests.business.pet_service import PetService
from src.cadastros.presentation.cadastros_routes import tutor_repo

router = APIRouter(prefix= "/pets", tags=["Pets"])

pet_repo= PetRepository()
pet_service= PetService(pet_repo, tutor_repo)

class PetCreateRequest(BaseModel):
    nome: str = Field(..., min_length= 2, description= "Nome do animal.")
    especie: str = Field(..., description= "Espécie, ecemplo: cachorro, gato.")
    raca: str = Field(None, description= "Raça de animal.")
    idade: int = Field(..., get= 0, description= "Idade do animal.")
    tutor_id: int = Field(..., description= "Id do tutor responsável.")

@router.post("", status_code=status.HTTP_201_CREATED)

def criar_pet(dados: PetCreateRequest):
    return pet_service.cadastrar_pet(
        nome= dados.nome,
        especie= dados.especie,
        raca= dados.raca,
        idade= dados.idade,
        tutor_id= dados.tutor_id
    )

@router.get("", status_code=status.HTTP_200_OK)
def listar_pests():
    return pet_service.listar_pets()