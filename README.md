Projeto Revenda de Carros (Car Dealer App)
Uma aplicação web Full-Stack desenvolvida para gerenciamento e exibição de veículos para venda. O sistema permite o cadastro de carros com imagens, visualização de detalhes, listagem de inventário e autenticação de usuários. O projeto foi arquitetado visando escalabilidade, utilizando PostgreSQL como banco de dados e Docker para containerização do ambiente.

Screenshots
(Espaço reservado para capturas de tela: Login, Lista de Carros, Detalhes do Veículo)

Tecnologias Utilizadas
Este projeto foi construído utilizando as seguintes tecnologias e conceitos:

Backend (Lógica e Dados)
Python 3: Linguagem principal.

Django Framework: Estrutura robusta para desenvolvimento web rápido e seguro.

Django ORM: Abstração de banco de dados.

PostgreSQL: Banco de dados relacional robusto para persistência dos dados.

Authentication System: Sistema de login e proteção de rotas nativo do Django.

Frontend (Interface)
Django Templates (MVT): Renderização dinâmica de páginas HTML.

HTML5: Estrutura semântica das páginas.

CSS3 & Flexbox: Estilização responsiva e layouts modernos.

Infraestrutura & DevOps
Docker: Containerização da aplicação para garantir consistência entre ambientes de desenvolvimento e produção.

Docker Compose: Orquestração dos containers (Web App e Banco de Dados).

Ferramentas
Virtualenv (venv): Isolamento de ambiente (caso não utilize Docker).

Git & GitHub: Controle de versão.

VS Code: Editor de código.

Funcionalidades
[x] Catálogo de Veículos: Listagem dinâmica de carros cadastrados.

[x] Página de Detalhes: Visualização completa das informações do veículo (Marca, Modelo, Ano, Preço).

[x] Gerenciamento de Mídia: Upload e exibição de fotos reais dos veículos.

[x] Sistema de Login: Acesso restrito para administradores ou usuários específicos.

[x] Painel Administrativo: Interface do Django Admin para cadastrar, editar e excluir carros.


Estrutura de Pastas (Resumo)

cars/
│
├── app/                 # Configurações principais (settings, urls)
├── cars/                # Aplicação de veículos (Models, Views)
├── media/               # Uploads de imagens (fotos dos carros)
├── static/              # Arquivos estáticos (CSS, JS)
├── templates/           # Arquivos HTML
├── Dockerfile           # Configuração da imagem Docker
├── docker-compose.yml   # Orquestração dos serviços
└── manage.py            # Script de gerenciamento do Django
