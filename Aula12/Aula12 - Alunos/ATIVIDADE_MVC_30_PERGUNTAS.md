# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: Pedro Gonçalves
- Turma: 3° Ano

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.
**Resposta:** Ficam na pasta `models/`.

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?
**Resposta:** O nome do arquivo é `streamflix.db`. Essa configuração está no arquivo `app.py` (na linha onde é definido `app.config["SQLALCHEMY_DATABASE_URI"]`).

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?
**Resposta:** Existem três classes principais: `FilmeFavorito` (no arquivo `models/filme_favorito.py`), `HistoricoBusca` (no arquivo `models/historico_busca.py`) e `ModeloBase` (no arquivo `models/base.py`).

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?
**Resposta:** Ambas herdam da superclasse `ModeloBase` (localizada em `models/base.py`). Por herança, elas ganham automaticamente os campos `id`, `data_criacao` e `data_atualizacao`.

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?
**Resposta:** O `__tablename__` é `"filmes_favoritos"`. Usamos `__tablename__` para definir explicitamente o nome da tabela no banco de dados, evitando que o SQLAlchemy tente adivinhar o nome a partir do nome da classe (o que poderia gerar nomes esquisitos ou fora do padrão).

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?
**Resposta:** A coluna é `tmdb_id`. Ela possui as restrições `nullable=False` (não pode ser nula) e `unique=True` (cada id deve ser único, não permitindo duplicatas na tabela).

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?
**Resposta:** O método primeiro verifica se o filme já está nos favoritos chamando `buscar_por_tmdb`. Se já existir, ele retorna `None`. Se não existir, ele cria uma nova instância de `FilmeFavorito` com os dados passados, adiciona essa instância à sessão do banco (`db.session.add`) e faz o commit para salvar efetivamente (`db.session.commit()`), retornando o novo objeto.

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?
**Resposta:** O método está no arquivo `models/historico_busca.py`, na classe `HistoricoBusca`. O nome do método é `ultimas`.

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.
**Resposta:** Ele grava apenas alguns campos espelhados. Os campos salvos são: `tmdb_id`, `titulo`, `poster_path`, `nota` (e também `ano`).

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?
**Resposta:** São exportados `ModeloBase`, `FilmeFavorito` e `HistoricoBusca` (através da variável `__all__`). O controller faz isso porque o `__init__.py` age como um arquivo centralizador, permitindo importar as classes diretamente do módulo `models` de forma mais limpa, sem precisar especificar o caminho de cada arquivo individual.

---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).
**Resposta:** Existem 3 Blueprints:
1. `favoritos` no arquivo `favoritos_controller.py` com `url_prefix="/favoritos"`.
2. `filmes` no arquivo `filmes_controller.py` com `url_prefix="/filmes"`.
3. `dashboard` no arquivo `dashboard_controller.py` sem `url_prefix` (responde na raiz `/`).

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?
**Resposta:** Está no arquivo `controllers/filmes_controller.py` e o nome da função é `populares()`.

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).
**Resposta:** Ela instancia a API (`api = TmdbApi()`), busca os filmes populares (`api.filmes_populares()`) e busca a lista de favoritos no banco (`FilmeFavorito.listar()`).

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?
**Resposta:** O `filmes_controller.py` registra o termo. Ele usa o model `HistoricoBusca` através da chamada `HistoricoBusca.registrar(termo, len(filmes))` por volta da linha 54.

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?
**Resposta:** É exigido o método `POST`. A URL completa de exemplo é `/favoritos/adicionar/550`.

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?
**Resposta:** O controller redireciona o usuário de volta para a lista de filmes populares (retornando `redirect(url_for("filmes.populares"))`).

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).
**Resposta:** São registrados no arquivo `app.py`. O comando usado é `app.register_blueprint()`, como por exemplo: `app.register_blueprint(dashboard_bp)`, `app.register_blueprint(filmes_bp)`, etc.

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?
**Resposta:** O controller é o `dashboard_controller.py`. Ele envia as variáveis `populares`, `melhores`, `total_favoritos`, `historico` e `modo_demo`.

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?
**Resposta:** Não é nenhum dos três; faz parte da camada de Serviço (Service). Ela é chamada pelos controllers (como `filmes_controller.py`) para se comunicar com a API do TMDB, encapsulando a complexidade da requisição HTTP externa e separando essa lógica da lógica de roteamento do Controller.

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.
**Resposta:** Vem de ambos, dependendo de como a busca for feita. Quando feita via formulário pelo botão, se o form method for GET, ele virá de `request.args`. Se o form submeter como POST (como verificado na rota), ele virá de `request.form`. O controller trata as duas formas: primeiro tenta `request.args.get("q")` (GET) e depois sobrescreve com `request.form.get("q")` se o método for POST.

---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?
**Resposta:** Ficam na pasta `views/templates/`. O caminho completo é `/home/pedrogonncalves/escola/3° Ano/Python/python/Aula12/Aula12 - Alunos/views/templates/`.

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?
**Resposta:** O template base é o `layout.html`. Os outros templates o usam por meio da tag Jinja `{% extends "layout.html" %}`.

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.
**Resposta:**
1. StreamFlix -> `{{ url_for('dashboard.index') }}`
2. Populares -> `{{ url_for('filmes.populares') }}`
3. Melhores -> `{{ url_for('filmes.melhores') }}`
4. Buscar -> `{{ url_for('filmes.buscar') }}`
5. Favoritos -> `{{ url_for('favoritos.listar') }}`

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?
**Resposta:** O arquivo é `views/templates/filmes/detalhe.html`. A variável `streaming` vem da função `detalhe` do controller `filmes_controller.py`, que por sua vez obtém os dados da API com `api.streaming(filme_id)`.

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?
**Resposta:** É um pedaço reutilizado (partial). Ele é incluído por arquivos como `index.html` e `filmes/lista.html` usando a tag Jinja `{% include "filmes/_card.html" %}`.

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?
**Resposta:** Ela sabe verificando a variável `favorito` passada pelo controller (`{% if favorito %}`). Se `favorito` não for nulo/vazio, significa que já está salvo e exibe o botão "Remover", caso contrário exibe o "Salvar".

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?
**Resposta:** O CSS está em `views/static/css/style.css`. O `layout.html` carrega o arquivo através da função Flask/Jinja `{{ url_for('static', filename='css/style.css') }}`.

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.
**Resposta:** O loop Jinja é `{% for fav in favoritos %}`. 3 campos exibidos na tabela são: Filme (`fav.titulo`), Nota (`fav.nota`) e Ano (`fav.ano`).

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?
**Resposta:** Significa que se a variável `modo_demo` for verdadeira, ele renderizará o bloco interno (que no caso exibe um aviso de demonstração informando a necessidade de usar o arquivo `.env`). A variável é disponibilizada globalmente pela função `inject_globals` decorada com `@app.context_processor` no arquivo `app.py`.

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.
**Resposta:** 
1. **View:** O usuário clica no botão "Salvar favorito" no arquivo `views/templates/filmes/detalhe.html`, que submete um formulário via POST.
2. **Controller:** A rota `/favoritos/adicionar/<tmdb_id>` no arquivo `controllers/favoritos_controller.py` recebe a requisição, extrai os dados do form e chama o Model.
3. **Model:** A função `FilmeFavorito.adicionar()` em `models/filme_favorito.py` recebe os dados, salva no banco e comita a transação (`db.session.commit()`).
4. **Retorno:** O `favoritos_controller.py` recebe o controle de volta e executa um `redirect(voltar)` (retornando para a tela detalhada de onde a requisição se originou).
