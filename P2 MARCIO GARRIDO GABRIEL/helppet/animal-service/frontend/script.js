const API_URL = "";

const container = document.getElementById("animaisContainer");
const btnCadastrar = document.getElementById("btnCadastrar");

async function carregarAnimais() {
  try {
    const response = await fetch(`${API_URL}/animals`);

    if (!response.ok) {
      throw new Error("Erro ao carregar animais");
    }

    const animais = await response.json();
    container.innerHTML = "";

    animais.forEach((animal) => {
      const card = document.createElement("div");
      card.className = "card";

      const statusEncontrado =
        animal.status === "Encontrado" || animal.encontrado === true;

      card.innerHTML = `
        <h3>${animal.nome}</h3>
        <p>📍 ${animal.cidade}</p>
        <p>Status: ${statusEncontrado ? "✅ Encontrado" : "❌ Perdido"}</p>
        ${
          !statusEncontrado
            ? `<button onclick="marcarEncontrado(${animal.id})">
                Marcar como encontrado
              </button>`
            : ""
        }
      `;

      container.appendChild(card);
    });
  } catch (error) {
    console.error(error);
    container.innerHTML = "<p>Não foi possível carregar os animais.</p>";
  }
}

async function cadastrarAnimal() {
  const nome = document.getElementById("nome").value.trim();
  const cidade = document.getElementById("cidade").value.trim();

  if (!nome || !cidade) {
    alert("Preencha todos os campos");
    return;
  }

  try {
    const response = await fetch(
      `${API_URL}/animals?nome=${encodeURIComponent(nome)}&cidade=${encodeURIComponent(cidade)}`,
      { method: "POST" }
    );

    if (!response.ok) {
      throw new Error("Erro ao cadastrar animal");
    }

    document.getElementById("nome").value = "";
    document.getElementById("cidade").value = "";

    await carregarAnimais();
  } catch (error) {
    console.error(error);
    alert("Erro ao cadastrar");
  }
}

async function marcarEncontrado(id) {
  try {
    const response = await fetch(`${API_URL}/animals/${id}/found`, {
      method: "PUT"
    });

    if (!response.ok) {
      throw new Error("Erro ao marcar como encontrado");
    }

    await carregarAnimais();
  } catch (error) {
    console.error(error);
    alert("Erro ao marcar como encontrado");
  }
}

btnCadastrar.addEventListener("click", cadastrarAnimal);

carregarAnimais();

window.marcarEncontrado = marcarEncontrado;