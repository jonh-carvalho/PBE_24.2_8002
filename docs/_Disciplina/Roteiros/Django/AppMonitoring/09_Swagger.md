### 1. Instalar as Dependências Necessárias

O `drf-yasg` usa a biblioteca `PyYAML` para a geração do schema OpenAPI. Caso ainda não esteja instalada, execute:

```bash
pip install PyYAML
```

### 2. Atualizar a Configuração no `urls.py`

Certifique-se de que o `urls.py` está configurado corretamente. Um exemplo de configuração de `urls.py` para evitar esse erro:

```python
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API de Conteúdos",
        default_version='v1',
        description="Documentação da API para o app de streaming de áudio e vídeo",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="suporte@exemplo.com"),
        license=openapi.License(name="Licença BSD"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Suas outras URLs
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),  # Inclua as URLs do seu app

    # URLs do Swagger
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

### 3. Reiniciar o Servidor

Após fazer essas mudanças, reinicie o servidor de desenvolvimento para garantir que as configurações sejam aplicadas:

```bash
python manage.py runserver
```

### 4. Verificar Acesso ao Swagger

Acesse `http://localhost:8000/swagger/` para visualizar a interface do Swagger. Se tudo estiver configurado corretamente, você deve ver a interface do Swagger.

### 5. Caso apareça o erro de template

Esse erro ocorre porque a configuração de arquivos estáticos (`STATIC_ROOT`) não está definida no seu `settings.py`. Para resolver, você precisa adicionar o caminho onde o Django armazenará os arquivos estáticos coletados quando você executar o comando `collectstatic`.

### 1. Configurar `STATIC_ROOT`

Adicione o seguinte no `settings.py`:

```python
import os

STATIC_URL = '/static/'

# Define o caminho para coletar arquivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

O `STATIC_ROOT` define o diretório onde todos os arquivos estáticos do projeto serão armazenados após você rodar `collectstatic`.

### 2. Executar `collectstatic`

Após definir o `STATIC_ROOT`, execute o comando abaixo para que o Django copie todos os arquivos estáticos para o diretório configurado em `STATIC_ROOT`:

```bash
python manage.py collectstatic
```

Esse comando é especialmente importante em ambientes de produção, mas você pode executá-lo em desenvolvimento para garantir que os arquivos estáticos estão no diretório correto.

### 3. Reiniciar o Servidor

Depois de definir o `STATIC_ROOT` e rodar `collectstatic`, reinicie o servidor Django:

```bash
python manage.py runserver
```

Esses passos devem resolver o erro, e você poderá acessar o Swagger sem problemas.