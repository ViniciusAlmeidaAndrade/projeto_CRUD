// URL base da sua API FastAPI
const API_URL = "http://127.0.0.1:8000";

// Função para formatar a data recebida da API
function formatarData(dataString) {
    if (!dataString) {
        return "Data Inválida";
    }
    const data = new Date(dataString);
    if (isNaN(data)) {
        return "Data Inválida";
    }
    const dia = String(data.getDate()).padStart(2, '0');
    const mes = String(data.getMonth() + 1).padStart(2, '0');
    const ano = data.getFullYear();
    return `${dia}/${mes}/${ano}`;
}

// Função para buscar e listar os projetos da API
async function fetchProjects() {
    try {
        const response = await fetch(`${API_URL}/projects/`);
        const projects = await response.json();

        const tableBody = document.getElementById("projects-table-body");
        tableBody.innerHTML = "";

        projects.forEach(project => {
            const row = document.createElement("tr");
            const formattedDate = formatarData(project.created_at);

            row.innerHTML = `
                <td>${project.id}</td>
                <td><a href="details.html?id=${project.id}">${project.name}</a></td>
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

// Função para carregar um projeto existente no formulário para edição
async function loadProjectForEditing() {
    const urlParams = new URLSearchParams(window.location.search);
    const projectId = urlParams.get('id');

    if (projectId) {
        document.getElementById('form-title').innerText = 'Editar Projeto';

        try {
            const response = await fetch(`${API_URL}/projects/${projectId}`);
            if (!response.ok) {
                throw new Error('Projeto não encontrado');
            }
            const project = await response.json();

            document.getElementById('name').value = project.name;
            document.getElementById('description').value = project.description;
            document.getElementById('status').value = project.status;

        } catch (error) {
            console.error('Erro ao carregar projeto:', error);
            alert('Erro ao carregar projeto para edição.');
        }
    }
}

// Função unificada para lidar com a submissão (criação e edição)
async function handleFormSubmit(event){
    event.preventDefault();

    const urlParams = new URLSearchParams(window.location.search);
    const projectId = urlParams.get('id');

    const name = document.getElementById("name").value;
    const description = document.getElementById("description").value;
    const status = document.getElementById("status").value;

    const projectData = {
        name: name,
        description: description,
        status: status
    };

    const method = projectId ? 'PATCH' : 'POST';
    const url = projectId ? `${API_URL}/projects/${projectId}` : `${API_URL}/projects/`;

    try {
        const response = await fetch(url, {
            method: method,
            headers: {"Content-Type": "application/json"},
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
async function deleteProject(projectId) {
    if (confirm("Tem certeza que deseja excluir este projeto?")) {
        try {
            const response = await fetch(`${API_URL}/projects/${projectId}`, {
                method: "DELETE",
            });
            if (response.ok) {
                alert("Projeto excluído com sucesso!");
                fetchProjects(); // Recarrega a lista de projetos
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

// NOVO: Função para carregar os detalhes de um projeto
async function loadProjectDetails() {
    const urlParams = new URLSearchParams(window.location.search);
    const projectId = urlParams.get('id');

    if (projectId) {
        try {
            const response = await fetch(`${API_URL}/projects/${projectId}`);
            if (!response.ok) {
                throw new Error('Projeto não encontrado');
            }
            const project = await response.json();

            // Preenche os elementos da página com os dados do projeto
            document.getElementById('project-title').innerText = project.name;
            document.getElementById('project-id').innerText = project.id;
            document.getElementById('project-name').innerText = project.name;
            document.getElementById('project-status').innerText = project.status;
            document.getElementById('project-created-at').innerText = formatarData(project.created_at);

        } catch (error) {
            console.error('Erro ao carregar detalhes do projeto:', error);
            alert('Erro ao carregar os detalhes do projeto.');
        }
    }
}

// Condicionais para executar a lógica correta em cada página
const projectForm = document.getElementById("project-form");
if (projectForm) {
    loadProjectForEditing();
    projectForm.addEventListener("submit", handleFormSubmit);
}

const projectTableBody = document.getElementById("projects-table-body");
if (projectTableBody) {
    fetchProjects();

    projectTableBody.addEventListener("click", (event) => {
        if (event.target.classList.contains("delete-button")) {
            const projectId = event.target.getAttribute("data-id");
            deleteProject(projectId);
        }
    });
}
const projectDetailsContainer = document.getElementById('project-title');
if(projectDetailsContainer){
    loadProjectDetails();
}