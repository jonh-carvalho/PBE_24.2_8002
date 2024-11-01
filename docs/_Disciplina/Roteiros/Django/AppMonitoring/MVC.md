Para criar um projeto ASP.NET Core MVC com um modelo `Employee` e usar o Entity Framework Core para acessar um banco de dados, siga as etapas abaixo:

### 1. Configuração do Projeto ASP.NET Core MVC
1. Abra o Visual Studio e selecione **Create a new project**.
2. Escolha **ASP.NET Core Web Application** e clique em **Next**.
3. Nomeie o projeto (por exemplo, `EmployeeManagement`) e selecione o local para salvá-lo.
4. Selecione o **Framework** como **.NET 6.0** (ou superior) e clique em **Create**.
5. Na próxima tela, escolha **Web Application (Model-View-Controller)** e marque **Enable Docker** se desejar suporte a Docker. Clique em **Create**.

### 2. Instalação do Entity Framework Core
Para usar o Entity Framework Core, você precisa instalar alguns pacotes:
1. Abra o **Package Manager Console** no Visual Studio (**Tools > NuGet Package Manager > Package Manager Console**).
2. Execute os seguintes comandos para instalar o EF Core e a biblioteca do provedor SQL Server:
   ```shell
   Install-Package Microsoft.EntityFrameworkCore
   Install-Package Microsoft.EntityFrameworkCore.SqlServer
   Install-Package Microsoft.EntityFrameworkCore.Tools
   ```

### 3. Criação do Modelo `Employee`
1. Na pasta **Models**, crie um novo arquivo chamado `Employee.cs` e adicione o seguinte código:
   ```csharp
   using System.ComponentModel.DataAnnotations;

   public class Employee
   {
       public int Id { get; set; }

       [Required]
       [StringLength(100)]
       public string Name { get; set; }

       [Required]
       [Range(18, 65)]
       public int Age { get; set; }

       [Required]
       [StringLength(50)]
       public string Position { get; set; }

       [Range(30000, 200000)]
       public decimal Salary { get; set; }
   }
   ```

### 4. Configuração do Contexto do Banco de Dados
1. Na pasta **Data**, crie uma nova classe chamada `AppDbContext.cs`:
   ```csharp
   using Microsoft.EntityFrameworkCore;

   public class AppDbContext : DbContext
   {
       public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

       public DbSet<Employee> Employees { get; set; }
   }
   ```

2. Adicione o contexto ao **Startup.cs** (ou `Program.cs`, dependendo da versão do ASP.NET Core):
   ```csharp
   using Microsoft.EntityFrameworkCore;

   var builder = WebApplication.CreateBuilder(args);

   // Configuração do banco de dados SQL Server
   builder.Services.AddDbContext<AppDbContext>(options =>
       options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

   var app = builder.Build();
   ```

3. Configure a **string de conexão** no arquivo `appsettings.json`:
   ```json
   "ConnectionStrings": {
       "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=EmployeeDB;Trusted_Connection=True;MultipleActiveResultSets=true"
   }
   ```

### 5. Criação da Migration e Atualização do Banco de Dados
No **Package Manager Console**, execute os seguintes comandos para criar a migração inicial e aplicar as alterações no banco de dados:
```shell
Add-Migration InitialCreate
Update-Database
```

### 6. Criação do Controller `EmployeeController`
1. Na pasta **Controllers**, clique com o botão direito e selecione **Add > Controller**.
2. Selecione **MVC Controller with views, using Entity Framework**.
3. Escolha o modelo `Employee` e o `AppDbContext` para o contexto de dados, e clique em **Add**.

Isso criará automaticamente um `EmployeeController` com ações CRUD e gerará as views correspondentes.

### 7. Configuração das Rotas e Teste da Aplicação
No `Program.cs`, certifique-se de que o mapeamento de rotas está configurado:
```csharp
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Employee}/{action=Index}/{id?}");

app.Run();
```

Agora você pode executar a aplicação e acessar o controlador `Employee` para adicionar, editar, excluir e listar funcionários usando o EF Core e ASP.NET Core MVC.