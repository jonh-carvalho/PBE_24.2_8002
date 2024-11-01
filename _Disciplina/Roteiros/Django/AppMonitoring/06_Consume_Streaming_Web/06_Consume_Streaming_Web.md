Vamos criar um simples app HTML e JavaScript que consome o endpoint `activities` da API Django REST que criamos anteriormente. Este app será responsável por listar as atividades retornadas pela API.

### 1. **Estrutura do Projeto**

Para organizar, vamos criar um arquivo HTML com JavaScript embutido para interagir com a API.

### 2. **Estrutura HTML Básica**

Crie um arquivo chamado `index.html`, onde vamos definir a estrutura da interface.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Activity Monitor</title>
  <style>
    body { font-family: Arial, sans-serif; }
    .activity-list { max-width: 600px; margin: auto; padding: 1em; }
    .activity { border: 1px solid #ccc; padding: 1em; margin-bottom: 1em; }
  </style>
</head>
<body>
  <h1>List of Activities</h1>
  <div id="activity-list" class="activity-list"></div>

  <script src="app.js"></script>
</body>
</html>
```

Neste arquivo:
- Definimos o elemento `<div id="activity-list">` onde as atividades serão listadas dinamicamente.
- Incluímos um arquivo JavaScript (`app.js`) onde escreveremos o código para consumir a API.

### 3. **JavaScript para Consumir a API**

Agora, vamos criar o arquivo `app.js` que fará a requisição ao endpoint `/api/activities/` e exibirá as atividades na página HTML.

Crie o arquivo `app.js`:

```javascript
// Define a URL base para o endpoint da API de atividades
const apiBaseURL = "http://127.0.0.1:8000/api/activities/";

// Função para buscar atividades da API
async function fetchActivities() {
  try {
    const response = await fetch(apiBaseURL);
    if (!response.ok) {
      throw new Error(`An error occurred: ${response.status}`);
    }
    const activities = await response.json();
    displayActivities(activities);
  } catch (error) {
    console.error("Failed to fetch activities:", error);
  }
}

// Função para exibir as atividades na página
function displayActivities(activities) {
  const activityList = document.getElementById("activity-list");
  activityList.innerHTML = ""; // Limpa a lista antes de adicionar atividades

  activities.forEach(activity => {
    const activityElement = document.createElement("div");
    activityElement.className = "activity";

    // Adicionando detalhes da atividade
    activityElement.innerHTML = `
      <h3>Activity Type: ${activity.activity_type}</h3>
      <p>Location: ${activity.location || "Not specified"}</p>
      <p>Description: ${activity.description || "No description"}</p>
      <p>Start Time: ${new Date(activity.start_time).toLocaleString()}</p>
      <p>End Time: ${new Date(activity.end_time).toLocaleString()}</p>
    `;

    // Adicionar as métricas da atividade se existirem
    if (activity.metrics) {
      activityElement.innerHTML += `
        <h4>Metrics:</h4>
        <p>Distance: ${activity.metrics.distance_km} km</p>
        <p>Duration: ${activity.metrics.duration_minutes} minutes</p>
        <p>Average Speed: ${activity.metrics.avg_speed_kmh} km/h</p>
        <p>Calories Burned: ${activity.metrics.calories_burned} kcal</p>
      `;
    }

    activityList.appendChild(activityElement);
  });
}

// Chamar a função de busca quando a página carregar
window.onload = fetchActivities;
```

### Explicação do Código

- `fetchActivities()`: Faz uma requisição `GET` para o endpoint `/api/activities/`, converte a resposta para JSON e passa os dados para a função `displayActivities`.
- `displayActivities(activities)`: Recebe a lista de atividades e as renderiza na página HTML.
- Para cada atividade:
  - Cria um `<div>` com classe `activity`.
  - Adiciona informações como tipo de atividade, localização, descrição e horário de início e término.
  - Caso existam métricas associadas à atividade, também as exibe.

### 4. **Testando o App**

1. **Certifique-se de que o servidor Django está em execução**:

   ```bash
   python manage.py runserver
   ```

2. Abra o arquivo `index.html` no navegador ou hospede-o em um servidor local (por exemplo, usando o **Live Server** do VSCode ou outro servidor local) para evitar problemas de CORS.

### 5. **Configurações Adicionais para CORS**

Caso o navegador apresente erros de CORS ao tentar acessar a API, configure o Django para permitir requisições de outros domínios. Instale `django-cors-headers`:

```bash
pip install django-cors-headers
```

Adicione `corsheaders` ao `INSTALLED_APPS` no `settings.py` e configure as permissões de CORS:

```python
INSTALLED_APPS = [
    # outros apps
    'corsheaders',
    'rest_framework',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # outros middlewares
]

CORS_ALLOW_ALL_ORIGINS = True  # Use somente para desenvolvimento
```

### Conclusão

Com esses arquivos, você criou um app simples em HTML e JavaScript que consome a API Django, exibindo as atividades esportivas no frontend. Para ampliar, você pode adicionar funcionalidades como paginação, filtros e detalhamento das atividades.