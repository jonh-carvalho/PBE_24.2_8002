## Criando um App REST Django para CRUD de Empregados: Um Guia Completo

**Entendendo o Desafio**

Criar um aplicativo REST Django para gerenciar um CRUD (Create, Read, Update, Delete) de empregados envolve a construção de uma API que permita as operações básicas de criação, leitura, atualização e exclusão de registros de funcionários.

**Arquitetura Básica**

1. **Django Backend:**
   * **Models:** Representam os dados de um empregado (nome, cargo, departamento, etc.).
   * **Views:** Exportam endpoints REST para as operações CRUD.
   * **Serializers:** Convertem os objetos Python (models) em formatos JSON para serem consumidos pelos clientes.

2. **Frontend:**
   * **Interface:** Uma interface web ou mobile para interagir com a API e exibir os dados.
   * **Requests:** Faz requisições HTTP para os endpoints da API para realizar as operações CRUD.

**Tecnologias Essenciais**

* **Django:** Framework Python para desenvolvimento web.
* **Django REST Framework (DRF):** Um poderoso toolkit para criar APIs RESTful em Django.

**Passo a Passo**

1. **Configuração do Django:**
   * Crie um novo projeto Django: `django-admin startproject myproject`
   * Crie um app dentro do projeto: `python manage.py startapp employees`
   * Instale o DRF: `pip install djangorestframework`
   * Adicione o DRF às INSTALLED_APPS no arquivo `settings.py` do seu projeto.

2. **Criação dos Models:**
   * Defina um modelo para representar um empregado:

   ```python
   from django.db import models

   class Employee(models.Model):
       name = models.CharField(max_length=100)
       role = models.CharField(max_length=100)
       department = models.CharField(max_length=100)
   ```

3. **Criação dos Serializers:**
   * Crie um serializer para converter o modelo Employee em JSON:

   ```python
   from rest_framework import serializers
   from .models import Employee

   class EmployeeSerializer(serializers.ModelSerializer):
       class Meta:
           model = Employee
           fields = '__all__'
   ```

4. **Criação das Views:**
   * Crie viewsets para as operações CRUD:

   ```python
   from rest_framework import viewsets
   from .models import Employee
   from .serializers import EmployeeSerializer

   class EmployeeViewSet(viewsets.ModelViewSet):
       queryset = Employee.objects.all()
       serializer_class = EmployeeSerializer
   ```

5. **Configuração das URLs:**
   * Inclua as URLs das views no arquivo `urls.py` do app:

   ```python
   from django.urls import path, include
   from rest_framework import routers
   from .views import EmployeeViewSet

   router = routers.DefaultRouter()
   router.register(r'employees', EmployeeViewSet)

   urlpatterns = [
       path('', include(router.urls)),
   ]
   ```

**Exemplo Completo:**

```python
# urls.py (projeto)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employees.urls')),
]
```

**Utilizando a API**

Com essa configuração básica, você já pode:

* **Criar um novo empregado:** Enviar uma requisição POST para `/employees/` com os dados no formato JSON.
* **Listar todos os empregados:** Enviar uma requisição GET para `/employees/`.
* **Obter um empregado específico:** Enviar uma requisição GET para `/employees/<id>/`.
* **Atualizar um empregado:** Enviar uma requisição PUT para `/employees/<id>/` com os novos dados.
* **Excluir um empregado:** Enviar uma requisição DELETE para `/employees/<id>/`.



