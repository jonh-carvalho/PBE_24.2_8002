// Função para buscar todas as atividades
async function fetchActivities() {
    const endpoint = 'http://127.0.0.1:8000/api/activities/';

    try {
      // Fazendo a requisição ao endpoint
      const response = await fetch(endpoint);

      if (!response.ok) {
        throw new Error("Erro ao buscar atividades.");
      }

      // Convertendo a resposta para JSON
      const activities = await response.json();

      // Exibindo as atividades na página
      displayActivities(activities);
    } catch (error) {
      console.error("Erro ao buscar atividades:", error);
    }
  }

  // Função para exibir as atividades
  function displayActivities(activities) {
    const container = document.getElementById("activity-container");
    container.innerHTML = ""; // Limpa o contêiner antes de exibir as atividades

    if (activities.length === 0) {
      container.innerHTML = "<p>Nenhuma atividade encontrada.</p>";
      return;
    }

    activities.forEach(activity => {
      // Criando o elemento HTML para cada atividade
      const activityElement = document.createElement("div");
      activityElement.className = "activity";

      // Definindo o conteúdo HTML para cada atividade
      activityElement.innerHTML = `
        <h3>${activity.activity_type_name || "Tipo não especificado"}</h3>
        <p><strong>Data de Início:</strong> ${new Date(activity.start_time).toLocaleString()}</p>
        <p><strong>Data de Término:</strong> ${new Date(activity.end_time).toLocaleString()}</p>
        <p><strong>Local:</strong> ${activity.location || "Local não especificado"}</p>
        <p><strong>Descrição:</strong> ${activity.description || "Sem descrição"}</p>
      `;

      container.appendChild(activityElement);
    });
  }
