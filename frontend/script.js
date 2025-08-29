// URL base da sua API FastAPI
const API_URL = "http://127.0.0.1:8000";

// Função para formatar a data recebida da API
function formatarData(dataString) {
    if (!dataString) {
        return "Data Inválida";
    }
    const data = new Date(dataString); // cria objeto Date
    if (isNaN(data)) {
        return "Data Inválida";
    }
    const dia = String(data.getDate()).padStart(2, '0');
    const mes = String(data.getMonth() + 1).padStart(2, '0'); // meses começam em 0
    const ano = data.getFullYear();
    return `${dia}/${mes}/${ano}`;
}


// Função para buscar e listar os projetos da API
async function fetchProjects() {
    try {
        const response = await fetch(`${API_URL}/projects/`);
        const projects = await response.json();

        const tableBody = document.getElementById("projects-table-body");
        tableBody.innerHTML = ""; // Limpa a tabela

        projects.forEach(project => {
            console.log("API retornou created_at:", project.created_at);
            const row = document.createElement("tr");
            const formattedDate = formatarData(project.created_at);

            row.innerHTML = `
                <td>${project.id}</td>
                <td><a href="details.html?id=${project.id}">${project.name}</a></td>
                <td>${project.description || ""}</td>
                <td>${project.status}</td>
                <td>${formattedDate}</td>
                <td>
                    <button>Editar</button>
                    <button>Excluir</button>
                </td>
            `;
            tableBody.appendChild(row);
        });

    } catch (error) {
        console.error("Erro ao buscar projetos:", error);
        alert("Ocorreu um erro ao conectar com o servidor para listar os projetos.");
    }
}

// Função para lidar com a submissão do formulário de criação de projetos
async function createProject(event){
    event.preventDefault();

    const name = document.getElementById("name").value;
    const description = document.getElementById("description").value;
    const status = document.getElementById("status").value;

    const projectData = {
        name: name,
        description: description,
        status: status
    };

    try {
        const response = await fetch(`${API_URL}/projects/`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(projectData),
        });
        if (response.ok) {
            alert("Projeto criado com sucesso!");
            window.location.href = "index.html";
            }else{
                const error = await response.json();
                alert("Erro ao criar projeto: " + error.detail);
            }
    } catch (error){
        console.error("Erro na requisição:", error);
        alert("Ocorreu um erro ao conectar com o servidor.");
    }
}

// Condicionais para executar a lógica correta em cada página
const projectForm = document.getElementById("project-form");
if (projectForm) {
    projectForm.addEventListener("submit", createProject);
}

const projectTableBody = document.getElementById("projects-table-body");
if (projectTableBody) {
    fetchProjects();
}