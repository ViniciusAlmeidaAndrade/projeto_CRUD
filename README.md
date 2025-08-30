# CRUD de Projetos - LTD

## Como Rodar o Projeto

Siga os passos abaixo para iniciar o backend e o frontend em sua máquina local.

### 1. Pré-requisitos

* **Python 3.10+**
* **PostgreSQL:** Certifique-se de que o servidor do PostgreSQL está instalado e rodando.
* **Git**
* **Virtualenv**

### 2. Configuração do Backend

1. Clonar o repositório
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto/backend

2.  Crie e ative um ambiente virtual:

    Crie com `python -m venv venv`  
    Ative com `source venv/bin/activate` (no macOS/Linux) ou `venv\Scripts\activate` (no Windows)

4. Navegue até a pasta do backend pelo seu terminal usando:
    `cd backend`


3.  Instale as dependências:
    `pip install fastapi uvicorn "uvicorn[standard]" "sqlalchemy[asyncio]" "psycopg2-binary" "python-multipart"`

4.  Verifique a sua string de conexão com o banco de dados no seu arquivo de backend. O formato deve ser parecido com:
    `"postgresql+psycopg2://user:password@localhost/database"`

5.  Execute o servidor FastAPI:
    `uvicorn main:app --reload`
    (Substitua `main` pelo nome do seu arquivo principal e `app` pelo nome da sua instância do FastAPI.)

### 3. Execução do Frontend

O frontend é composto por arquivos estáticos. Para acessá-lo:
1.  Navegue até a pasta `frontend`.
2.  Abra o arquivo `index.html` em seu navegador.