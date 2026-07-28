<div align="center">

# 🐍 Python — 3° Ano

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
<img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
<img src="https://img.shields.io/badge/Jinja2-Templates-B41717?style=for-the-badge&logo=jinja&logoColor=white" alt="Jinja2">
<img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">

---

Repositório com todos os projetos e atividades da disciplina de **Python** do **3° Ano — Técnico em Informática** no Cotemig.

Abrange desde os fundamentos do Flask até a construção de APIs RESTful, passando por padrão MVC, templates Jinja2 e persistência com SQLAlchemy.

</div>

---

## 📂 Estrutura do Repositório

```
python/
│
├── 📄 atividade1.py              # Atividade sobre Decorators no Flask
├── 📄 curriculo.py               # Currículo web premium com Flask
│
├── 📁 aula3/                     # Templates HTML com render_template
├── 📁 Aula4/                     # Formulários e métodos HTTP (GET/POST)
├── 📁 Aula7/                     # Calculadora web com Flask
├── 📁 Aula8/                     # Painel de especialidades médicas
├── 📁 aula_jinja/                # Templates Jinja2 (herança e loops)
│
├── 📁 SQLAlchemy/                # Introdução ao SQLAlchemy com Flask
├── 📁 SQLAlchemy_Completo/       # Exercícios de correção de código SQLAlchemy
│
├── 📁 Aula10/                    # Calculadora MVC com persistência
├── 📁 Aula12/                    # StreamFlix — Atividade MVC (30 questões)
│
├── 📁 atividade_avaliativa/      # 🎬 Sistema de Cinema — Atividade Avaliativa
├── 📁 revisao1/                  # ⚽ Sistema de Jogadores — Revisão
├── 📁 Aula15-API/                # 📚 API REST de Livros (JSON / Postman)
│
└── 📄 .gitignore
```

---

## 🗂️ Detalhes das Aulas & Projetos

### 🔰 Fundamentos

| Aula / Arquivo | Descrição | Conceitos |
|---|---|---|
| `atividade1.py` | Explicação de Decorators via rota Flask | `@app.route`, decorators |
| `curriculo.py` | Currículo web pessoal estilizado | HTML inline, CSS moderno, glassmorphism |
| `aula3/` | Primeira aplicação com templates | `render_template`, HTML externo |
| `Aula4/` | Sistema de login com formulário | `request`, `GET` / `POST` |

---

### ⚙️ Intermediário

| Aula / Pasta | Descrição | Conceitos |
|---|---|---|
| `Aula7/` | Calculadora web | Modularização, formulários |
| `Aula8/` | Painel de médicos e especialidades | Dicionários, filtros, Jinja2 |
| `aula_jinja/` | Exercícios de templates Jinja2 | Template inheritance, `{% for %}`, `{% block %}` |
| `SQLAlchemy/` | CRUD de alunos com banco SQLite | Flask-SQLAlchemy, ORM |
| `SQLAlchemy_Completo/` | 5 exercícios de correção de código | Debug, configuração, CRUD |

---

### 🏗️ Avançado — Padrão MVC

| Aula / Pasta | Descrição | Conceitos |
|---|---|---|
| `Aula10/` | Calculadora com arquitetura MVC | Models, Controllers, Blueprints |
| `Aula12/` | StreamFlix — 30 questões sobre MVC | Teoria MVC, boas práticas |
| `atividade_avaliativa/` | **Sistema de Cinema** — Filmes, Salas, Sessões e Ingressos | MVC completo, relacionamentos, dashboard |
| `revisao1/` | **Sistema de Jogadores** — CRUD completo | MVC, dados iniciais, dashboard |
| `Aula15-API/` | **API REST de Livros** — Endpoints JSON | API RESTful, `jsonify`, Postman |

---

## 🚀 Como Executar

### Pré-requisitos

- **Python 3.8+**
- **pip** (gerenciador de pacotes)

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/pedrinngkl/python.git
cd python

# 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 3. Instale as dependências do projeto desejado
pip install -r <pasta>/requirements.txt
# Exemplo: pip install -r Aula15-API/requirements.txt

# 4. Execute a aplicação
python <pasta>/app.py
# Exemplo: python Aula15-API/app.py
```

> 💡 A aplicação estará disponível em **http://127.0.0.1:5000**

---

## 🛠️ Tecnologias Utilizadas

<table align="center">
  <tr>
    <td align="center" width="120">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="48" height="48" alt="Python" />
      <br><strong>Python</strong>
    </td>
    <td align="center" width="120">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="48" height="48" alt="Flask" />
      <br><strong>Flask</strong>
    </td>
    <td align="center" width="120">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" width="48" height="48" alt="SQLAlchemy" />
      <br><strong>SQLAlchemy</strong>
    </td>
    <td align="center" width="120">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="48" height="48" alt="SQLite" />
      <br><strong>SQLite</strong>
    </td>
    <td align="center" width="120">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="48" height="48" alt="HTML5" />
      <br><strong>HTML5</strong>
    </td>
    <td align="center" width="120">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="48" height="48" alt="CSS3" />
      <br><strong>CSS3</strong>
    </td>
  </tr>
</table>

---

## 📌 Padrão Arquitetural

Os projetos mais avançados seguem o padrão **MVC (Model-View-Controller)**:

```
projeto/
├── models/          # Modelos de dados (SQLAlchemy)
│   ├── __init__.py
│   ├── base.py
│   └── entidade.py
│
├── controllers/     # Lógica de rotas (Blueprints)
│   ├── __init__.py
│   └── entidade_controller.py
│
├── views/           # Interface (Templates Jinja2)
│   ├── templates/
│   └── static/
│
└── app.py           # Ponto de entrada da aplicação
```

---

## 👨‍💻 Autor

<div align="center">

**Pedro Gonçalves**


[![GitHub](https://img.shields.io/badge/GitHub-pedrinngkl-181717?style=flat-square&logo=github)](https://github.com/pedrinngkl)
[![Email](https://img.shields.io/badge/Email-pedrogpereira9%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:pedrogpereira9@gmail.com)

</div>

---

<div align="center">
  <sub>Feito com ❤️ e ☕ durante o 3° Ano — 2026</sub>
</div>
