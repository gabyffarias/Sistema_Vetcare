from fastapi import FastAPI
from src.auth.presentation.auth_routes import router as auth_router
from src.cadastros.presentation.cadastros_routes import router as cadastros_router
from src.pests.presentation.pets_routes import router as pets_router


app= FastAPI(
    title= "VetCare API",
    description= "Sistema de gestão para clínica veterinária - Monolito modular",
    version= "1.0.0"
)

app.include_router(auth_router, prefix= "/auth", tags=["Autenticação"])
app.include_router(cadastros_router, prefix= "/cadastros", tags= ["Cadastros"])
app.include_router(pets_router)

@app.get("/")
def read_root():
    return{"messsage": "Bem vindo à API do Vetcare! Sistema rodando com sucesso."}