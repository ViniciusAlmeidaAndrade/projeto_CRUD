# CRUD de Projetos - LTD  

Esse projeto é um CRUD para projetos feito em **FastAPI**.  
A aplicação permite que o usuário adicione projetos, liste todos os que estão no banco de dados, edite projetos existentes e remova-os.  

---
## Autenticação

O sistema utiliza autenticação via JWT. Para acessar as rotas protegidas do CRUD de projetos, é necessário realizar login.

Para testes, um usuário padrão já pode ser usado:

- Email: admin@exemplo.com
- Senha: admin

O token gerado no login deve ser salvo no localStorage pelo frontend, permitindo o acesso às páginas protegidas.

---

## Como Rodar o Projeto

Siga os passos abaixo para iniciar o backend e o frontend em sua máquina local.

---

### 1. Pré-requisitos

* **Python 3.10+**
* **PostgreSQL**
* **Git**
* **Virtualenv**

---

### 2. Configuração do Backend

1. **Clonar o repositório**
   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd seu-projeto/backend
   ```

2. **Criar e ativar o ambiente virtual**
   ```bash
   python -m venv venv
   ```
   - Ativar no macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Ativar no Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Instalar as dependências**
   ```bash
   pip install fastapi uvicorn "uvicorn[standard]" "sqlalchemy[asyncio]" "psycopg2-binary" "python-multipart" alembic
   ```

4. **Verificar/ajustar a string de conexão com o banco**  
   O formato deve ser parecido com:
   ```env
   postgresql+psycopg2://usuario:senha@localhost/projetos_db
   ```

5. **Executar o servidor FastAPI**
   ```bash
   uvicorn main:app --reload
   ```

---

### 3. Banco de Dados

1. **Instale o PostgreSQL** se ainda não tiver download aqui (https://www.postgresql.org/download/).

2. **Crie o banco de dados**:
   ```sql
   CREATE DATABASE projetos_db;
   ```

3. **Configure a string de conexão** no código ou em um arquivo `.env`:
   ```env
   DATABASE_URL=postgresql+psycopg2://postgres:senha@localhost/projetos_db
   ```
   > Obs.: Altere `postgres` e `senha` para os dados do seu PostgreSQL local.

4. **Execute as migrations** para criar as tabelas automaticamente:
   ```bash
   alembic upgrade head
   ```

---

### 4. Execução do Frontend

O frontend é composto por arquivos estáticos. Para acessá-lo:

1. Navegue até a pasta `frontend`.
2. Abra o arquivo `index.html` em seu navegador.

---

### 5. Testando a API

Após rodar o backend, acesse no navegador:
```
http://127.0.0.1:8000/docs
```
Lá você encontrará a documentação interativa da API (Swagger UI), onde é possível testar os endpoints de **criar, listar, editar e remover projetos**.

---

### 6. Login no Frontend

Para acessar as funcionalidades do CRUD via frontend, siga os passos:

1. Abra `login.html`.
2. Insira o email e senha do usuário.
3. Ao logar, um token será armazenado no localStorage.
4. Com o token válido, você poderá:
   - Listar projetos (`index.html`)
   - Visualizar detalhes (`detalhes.html`)
   - Criar/editar projetos (`form.html`)
   - Excluir projetos diretamente da tabela

## 📌 Observações

- O backend só funcionará se o PostgreSQL estiver rodando e o banco tiver sido criado.  
- Certifique-se de ativar o ambiente virtual sempre que for iniciar o backend.  
- As migrations já estão configuradas no projeto, então basta rodar `alembic upgrade head` para criar/atualizar as tabelas.
- Se o token expirar ou for inválido, o usuário será redirecionado para a página de login.
- Todas as rotas do CRUD requerem autenticação, então é necessário logar antes de acessar qualquer funcionalidade.