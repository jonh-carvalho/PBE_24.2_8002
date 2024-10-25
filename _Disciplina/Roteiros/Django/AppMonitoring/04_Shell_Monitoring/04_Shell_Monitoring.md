O Django Shell é uma ferramenta poderosa que permite interagir com o banco de dados e os componentes do Django diretamente na linha de comando, ideal para testar modelos, criar dados de exemplo, ou depurar problemas sem a necessidade de criar views e templates. No contexto do nosso app de monitoramento de atividades esportivas, o Django Shell pode ser útil para:

1. **Criar e Manipular Instâncias de Modelos**,
2. **Consultar Dados**,
3. **Atualizar e Excluir Dados**,
4. **Explorar Relacionamentos entre Modelos**.

Aqui estão alguns exemplos de como utilizar o Django Shell com as classes que criamos.

### 1. **Iniciando o Django Shell**
Para abrir o Django Shell, execute o comando abaixo:

```bash
python manage.py shell
```

### 2. **Importar os Modelos**
Após abrir o shell, importe os modelos que vamos utilizar:

```python
from django.contrib.auth.models import User
from activities.models import Activity, ActivityType, ActivityMetrics, ActivityHistory
```

### 3. **Criando Instâncias de Modelos**
Primeiro, vamos criar um usuário para associá-lo às atividades esportivas.

#### Criando um Usuário

```python
user = User.objects.create_user(username='john_doe', email='john@example.com', password='password123')
```

#### Criando um Tipo de Atividade

```python
running_type = ActivityType.objects.create(name='Running', description='Running activity')
cycling_type = ActivityType.objects.create(name='Cycling', description='Cycling activity')
```

#### Criando uma Atividade e Métricas Associadas

Podemos criar uma atividade de corrida e associá-la ao usuário e tipo de atividade que criamos.

```python
from datetime import datetime, timedelta

# Criando uma nova atividade
activity = Activity.objects.create(
    user=user,
    activity_type=running_type,
    start_time=datetime(2023, 1, 1, 7, 0),
    end_time=datetime(2023, 1, 1, 8, 0),
    location="Central Park",
    description="Morning run"
)

# Criando métricas para essa atividade
metrics = ActivityMetrics.objects.create(
    activity=activity,
    distance_km=5.0,
    duration_minutes=60,
    avg_speed_kmh=5.0,
    calories_burned=300
)
```

### 4. **Consultando Dados**

#### Listando Todas as Atividades de um Usuário

```python
activities = Activity.objects.filter(user=user)
for activity in activities:
    print(activity)
```

#### Consultando Métricas de uma Atividade

```python
metrics = ActivityMetrics.objects.get(activity=activity)
print(f"Distance: {metrics.distance_km} km, Calories burned: {metrics.calories_burned}")
```

### 5. **Explorando Relacionamentos entre Modelos**

#### Acessar Todas as Atividades de um Tipo Específico (Exemplo: Corrida)

```python
running_activities = Activity.objects.filter(activity_type=running_type)
for act in running_activities:
    print(f"{act.user.username} ran at {act.location} on {act.start_time}")
```

#### Consultar Histórico de Atividades do Usuário

Primeiro, criaremos registros de histórico para esse usuário:

```python
history_entry = ActivityHistory.objects.create(user=user, activity=activity)
```

Agora, para listar o histórico de atividades do usuário:

```python
history = ActivityHistory.objects.filter(user=user)
for entry in history:
    print(f"Activity on {entry.created_at}: {entry.activity.description}")
```

### 6. **Atualizando Dados**

#### Atualizar a Distância de uma Atividade

Vamos dizer que o usuário registrou incorretamente a distância da corrida e precisamos atualizá-la.

```python
metrics = ActivityMetrics.objects.get(activity=activity)
metrics.distance_km = 5.5
metrics.save()
print(f"Updated distance: {metrics.distance_km} km")
```

### 7. **Excluindo Dados**

#### Excluir uma Atividade

Se o usuário deseja remover uma atividade, você pode fazer isso facilmente no shell.

```python
activity_to_delete = Activity.objects.get(id=activity.id)
activity_to_delete.delete()
```

### 8. **Consultas Avançadas com Filtros**

#### Atividades por Duração e Calorias

Suponha que você queira todas as atividades onde a duração foi superior a 30 minutos e as calorias queimadas foram acima de 250.

```python
filtered_activities = ActivityMetrics.objects.filter(duration_minutes__gt=30, calories_burned__gt=250)
for act_metrics in filtered_activities:
    print(f"Activity: {act_metrics.activity.description}, Calories: {act_metrics.calories_burned}")
```

### 9. **Utilizando Anotações e Agregações**

#### Média de Velocidade em Atividades de Corrida

Para calcular a média de velocidade em atividades de corrida para um usuário:

```python
from django.db.models import Avg

average_speed = ActivityMetrics.objects.filter(activity__activity_type=running_type).aggregate(Avg('avg_speed_kmh'))
print(f"Average Running Speed: {average_speed['avg_speed_kmh__avg']} km/h")
```

### Resumo

Essas operações demonstram o potencial do Django Shell para testar interações e manipulações de dados no desenvolvimento do app de monitoramento de atividades esportivas, auxiliando em cenários como:

- **Inserção de dados** para criar e vincular atividades e métricas;
- **Consultas** complexas para ver histórico de atividades e resultados;
- **Atualizações e exclusões** para ajuste de informações;
- **Exploração de relacionamentos** para consultas cruzadas.

Essas práticas também ajudam a garantir que a lógica do app está correta antes de implementar a interface da API REST.