# Sistema VetCare

Sistema de gestão para clínica veterinária desenvolvido para a disciplina de Engenharia de Software I (UFBA).

# VetCare API - Sistema de Gestão Veterinária

Sistema desenvolvido em Python com FastAPI para a gestão de tutores, animais (pets) e atendimentos veterinários.

# Como Executar o Projeto

No seu terminal siga os passos abaixo para rodar a aplicação em sua máquina local:

# 1. Clonar o repositório

Abra uma pasta nomeada como: Sistema_Vetcare

**No terminal** abra a pasta com: cd Sistema_Vetcare

Depois copie o link do Github para clonar o repositório e aplique no terminal : 

git clone [https://github.com/SEU_USUARIO/Sistema_Vetcare.git]

# 2. Criar e ativar ambiente Virtual

*No windows*

python -m venv venv
venv\Scripts\Activate

*No linux*
python3 -m venv venv
source venv/bin/activate

# 3. Instalar as dependências 

pip install fastapi uvicorn pydantic

# 4. Executar a API

uvicorn src.main:app --reload

**OBS**: Verifique de que está na pasta raiz do projeto

# Documentação interativa (swagger UI)

Com o servidor rodando, você pode testar todas as rotas diretamente pelo navegador através da documentação interativa gerada automaticamente pelo FastAPI:

Swagger UI: http://127.0.0.1:8000/docs