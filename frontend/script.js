// URL base da sua API FastAPI
const API_URL = "http://127.0.0.1:8000";

// Função de login para geral token e salvar  no localStorage
async function loginUser(event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try{

        const response = await fetch(`${API_URL}/autenticacao/login`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        const data = await response.json();
        if (response.ok) {
            localStorage.setItem("token", data.access_token);
            alert("Login realizado com sucesso!");
            window.location.href = "index.html";
        }else{
            document.getElementById("login-msg").innerText = data.datail || "Erro no login";
        }
    } catch (error){
        console.error("Erro no login:", error);
        alert("Ocorreu um erro ao tentar logar")
    }
}

//função para checar se o usuario está logado para poder ter acesso a pagina
async function checkAuth() {
    const token = localStorage.getItem("token");
    if (!token) {
        alert("Você precisa estar logado para acessar essa página.");
        window.location.href = "login.html";
        return false;
    }

    try {
        // Chama uma rota protegida pra validar o token
        const response = await fetch("http://127.0.0.1:8000/projects/", {
            headers: { "Authorization": `Bearer ${token}` }
        });

        if (!response.ok) {
            // Token inválido ou expirado
            localStorage.removeItem("token");
            alert("Sessão expirada, faça login novamente.");
            window.location.href = "login.html";
            return false;
        }

        return true; // token válido
    } catch (err) {
        console.error("Erro ao validar token:", err);
        window.location.href = "login.html";
        return false;
    }
}

// função para garantir login antes de qualquer reload da pagina
const loginForm = document.getElementById("login-form");
if (loginForm) {
    loginForm.addEventListener("submit", loginUser);
}

// Função para formatar a data recebida da API
function formateDate(dataString) {

    if (!dataString) {
        return "Data Inválida";
    }
    const data = new Date(dataString);
    if (isNaN(data)) {
        return "Data Inválida";
    }
    const dia = String(data.getDate()).padStart(2, "0");
    const mes = String(data.getMonth() + 1).padStart(2, "0");
    const ano = data.getFullYear();
    return `${dia}/${mes}/${ano}`;
}

// Função para buscar e listar os projetos da API
async function listProjects() {

    try {
        const token = localStorage.getItem("token");
        const response = await fetch(`${API_URL}/projects/`,{
            headers: { "Authorization": `Bearer ${token}` }
        });
        const projects = await response.json();

        const tableBody = document.getElementById("projects-table-body");
        tableBody.innerHTML = "";

        projects.forEach(project => {
            const row = document.createElement("tr");
            const formattedDate = formateDate(project.created_at);

            row.innerHTML = `
                <td>${project.id}</td>
                <td><a href="detalhes.html?id=${project.id}">${project.name}</a></td>
                <td>${project.status}</td>
                <td>${formattedDate}</td>
                <td>
                    <a href="form.html?id=${project.id}"><button>Editar</button></a>
                    <button class="delete-button" data-id="${project.id}">Excluir</button>
                </td>
            `;
            tableBody.appendChild(row);
        });

    } catch (error) {
        console.error("Erro ao buscar projetos:", error);
        alert("Ocorreu um erro ao conectar com o servidor para listar os projetos.");
    }
}

// Função para carregar os detalhes de um projeto
async function DetailsProject() {

    const urlParams = new URLSearchParams(window.location.search);
    const projectId = urlParams.get("id");

    if (projectId) {
        try {
            const token = localStorage.getItem("token");
            const response = await fetch(`${API_URL}/projects/${projectId}`,{
                headers: { "Authorization": `Bearer ${token}` }
            });
            if (!response.ok) {
                throw new Error("Projeto não encontrado");
            }
            const project = await response.json();

            document.getElementById("project-title").innerText = project.name;
            document.getElementById("project-id").innerText = project.id;
            document.getElementById("project-name").innerText = project.name;
            document.getElementById("project-description").innerText = project.description;
            document.getElementById("project-status").innerText = project.status;
            document.getElementById("project-created-at").innerText = formateDate(project.created_at);

        } catch (error) {
            console.error("Erro ao carregar detalhes do projeto:", error);
            alert("Erro ao carregar os detalhes do projeto.");
        }
    }
}

// Função para carregar um projeto existente no formulário para edição
async function EditingProject() {

    const token = localStorage.getItem("token");
    const urlParams = new URLSearchParams(window.location.search);
    const projectId = urlParams.get("id", {
         headers: { "Authorization": `Bearer ${token}` }
    });

    if (projectId) {
        document.getElementById("form-title").innerText = "Editar Projeto";

        try {
            const token = localStorage.getItem("token");
            const response = await fetch(`${API_URL}/projects/${projectId}`,{
                headers: { "Authorization": `Bearer ${token}` }
            });
            if (!response.ok) {
                throw new Error("Projeto não encontrado");
            }
            const project = await response.json();

            document.getElementById("name").value = project.name;
            document.getElementById("description").value = project.description;
            document.getElementById("status").value = project.status;

        } catch (error) {
            console.error("Erro ao carregar projeto:", error);
            alert("Erro ao carregar projeto para edição.");
        }
    }
}

// Função unificada para lidar com a submissão (criação e edição)
async function FormSubmit(event){
    event.preventDefault();

    const token = localStorage.getItem("token");
    const urlParams = new URLSearchParams(window.location.search);
    const projectId = urlParams.get("id");
    const name = document.getElementById("name").value;
    const description = document.getElementById("description").value;
    const status = document.getElementById("status").value;

    const projectData = {
        name: name,
        description: description,
        status: status
    };

    const method = projectId ? "PATCH" : "POST";
    const url = projectId ? `${API_URL}/projects/${projectId}` : `${API_URL}/projects/`;

    try {
        const response = await fetch(url, {
            method: method,
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify(projectData),
        });
        if (response.ok) {
            alert("Projeto salvo com sucesso!");
            window.location.href = "index.html";
        }else{
            const error = await response.json();
            alert("Erro ao salvar projeto: " + error.detail);
        }
    } catch (error){
        console.error("Erro na requisição:", error);
        alert("Ocorreu um erro ao conectar com o servidor.");
    }
}

// Função para deletar um projeto
async function deleteProject(projectId) {

    if (confirm("Tem certeza que deseja excluir este projeto?")) {
        try {
            const token = localStorage.getItem("token");
            const response = await fetch(`${API_URL}/projects/${projectId}`, {
                headers: { "Authorization": `Bearer ${token}` },
                method: "DELETE"
            });
            if (response.ok) {
                alert("Projeto excluído com sucesso!");
                listProjects(); // Recarrega a lista de projetos
            } else {
                const error = await response.json();
                alert("Erro ao excluir projeto: " + error.detail);
            }
        } catch (error) {
            console.error("Erro na requisição:", error);
            alert("Ocorreu um erro ao conectar com o servidor.");
        }
    }
}

// Condicionais para executar a lógica correta em cada página
const projectForm = document.getElementById("project-form");
if (projectForm) {
    EditingProject();
    projectForm.addEventListener("submit", FormSubmit);
}

const projectTableBody = document.getElementById("projects-table-body");
if (projectTableBody) {
    listProjects();

    projectTableBody.addEventListener("click", (event) => {
        if (event.target.classList.contains("delete-button")) {
            const projectId = event.target.getAttribute("data-id");
            deleteProject(projectId);
        }
    });
}
const projectDetailsContainer = document.getElementById("project-title");
if(projectDetailsContainer){
    DetailsProject();
}