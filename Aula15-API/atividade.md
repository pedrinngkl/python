# Atividade — Aula 15: API REST (Flask)

## Descrição

Nesta atividade, utilizamos a API REST desenvolvida em Flask para realizar operações CRUD (Create, Read, Update, Delete) sobre a entidade **Livro**.

**Observação:** Não há frontend nesta atividade. Todas as operações foram realizadas via terminal (curl / Invoke-RestMethod).

---

## 1. POST — Inserção de 15 Livros Novos

Foram inseridos 15 livros utilizando o método POST:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":ANO}'
```

### Livros inseridos:

| # | Título | Autor | Ano |
|---|--------|-------|-----|
| 1 | O Alquimista | Paulo Coelho | 1988 |
| 2 | Harry Potter e a Pedra Filosofal | J.K. Rowling | 1997 |
| 3 | O Senhor dos Anéis | J.R.R. Tolkien | 1954 |
| 4 | Cem Anos de Solidão | Gabriel García Márquez | 1967 |
| 5 | A Revolução dos Bichos | George Orwell | 1945 |
| 6 | O Pequeno Príncipe | Antoine de Saint-Exupéry | 1943 |
| 7 | Cotemig | 3A1 | 2026 |
| 8 | Memórias Póstumas de Brás Cubas | Machado de Assis | 1881 |
| 9 | Grande Sertão: Veredas | Guimarães Rosa | 1956 |
| 10 | Capitães da Areia | Jorge Amado | 1937 |
| 11 | Vidas Secas | Graciliano Ramos | 1938 |
| 12 | A Hora da Estrela | Clarice Lispector | 1977 |
| 13 | O Auto da Compadecida | Ariano Suassuna | 1955 |
| 14 | Iracema | José de Alencar | 1865 |
| 15 | Macunaíma | Mário de Andrade | 1928 |

---

## 2. PUT — Atualização do Livro ID 1

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/livros/1 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"titulo":"Cotemig","autor":"3A1","ano":2026}'
```

**Resultado:**

```
ano          : 2026
autor        : 3A1
data_criacao : 2026-07-28 10:10:30.698283
id           : 1
titulo       : Cotemig
```

---

## 3. GET — Lista completa após POST + PUT

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/livros
```

**Resultado:**

```
ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-28 10:10:30.698295
id           : 3
titulo       : 1984

ano          : 1977
autor        : Clarice Lispector
data_criacao : 2026-07-28 10:10:59.597062
id           : 15
titulo       : A Hora da Estrela

ano          : 1945
autor        : George Orwell
data_criacao : 2026-07-28 10:10:59.446706
id           : 8
titulo       : A Revolução dos Bichos

ano          : 1937
autor        : Jorge Amado
data_criacao : 2026-07-28 10:10:59.560162
id           : 13
titulo       : Capitães da Areia

ano          : 1967
autor        : Gabriel García Márquez
data_criacao : 2026-07-28 10:10:59.422592
id           : 7
titulo       : Cem Anos de Solidão

ano          : 2026
autor        : 3A1
data_criacao : 2026-07-28 10:10:30.698283
id           : 1
titulo       : Cotemig

ano          : 2026
autor        : 3A1
data_criacao : 2026-07-28 10:10:59.494213
id           : 10
titulo       : Cotemig

ano          : 1956
autor        : Guimarães Rosa
data_criacao : 2026-07-28 10:10:59.536666
id           : 12
titulo       : Grande Sertão: Veredas

ano          : 1997
autor        : J.K. Rowling
data_criacao : 2026-07-28 10:10:59.370295
id           : 5
titulo       : Harry Potter e a Pedra Filosofal

ano          : 1865
autor        : José de Alencar
data_criacao : 2026-07-28 10:10:59.630913
id           : 17
titulo       : Iracema

ano          : 1928
autor        : Mário de Andrade
data_criacao : 2026-07-28 10:10:59.648227
id           : 18
titulo       : Macunaíma

ano          : 1881
autor        : Machado de Assis
data_criacao : 2026-07-28 10:10:59.517262
id           : 11
titulo       : Memórias Póstumas de Brás Cubas

ano          : 1988
autor        : Paulo Coelho
data_criacao : 2026-07-28 10:10:59.341094
id           : 4
titulo       : O Alquimista

ano          : 1955
autor        : Ariano Suassuna
data_criacao : 2026-07-28 10:10:59.612616
id           : 16
titulo       : O Auto da Compadecida

ano          : 1890
autor        : Aluísio Azevedo
data_criacao : 2026-07-28 10:10:30.698293
id           : 2
titulo       : O Cortiço

ano          : 1943
autor        : Antoine de Saint-Exupéry
data_criacao : 2026-07-28 10:10:59.470523
id           : 9
titulo       : O Pequeno Príncipe

ano          : 1954
autor        : J.R.R. Tolkien
data_criacao : 2026-07-28 10:10:59.396316
id           : 6
titulo       : O Senhor dos Anéis

ano          : 1938
autor        : Graciliano Ramos
data_criacao : 2026-07-28 10:10:59.579322
id           : 14
titulo       : Vidas Secas
```

**Total: 18 livros** (3 iniciais + 15 inseridos, com ID 1 atualizado via PUT)

---

## 4. DELETE — Remoção dos índices 5, 6 e 7

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/livros/5 -Method DELETE
Invoke-RestMethod http://127.0.0.1:5000/api/livros/6 -Method DELETE
Invoke-RestMethod http://127.0.0.1:5000/api/livros/7 -Method DELETE
```

**Livros removidos:**
- **ID 5** — Harry Potter e a Pedra Filosofal (J.K. Rowling, 1997)
- **ID 6** — O Senhor dos Anéis (J.R.R. Tolkien, 1954)
- **ID 7** — Cem Anos de Solidão (Gabriel García Márquez, 1967)

Todos retornaram **HTTP 204 (No Content)** — exclusão bem-sucedida.

---

## 5. GET — Lista completa após DELETE

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/livros
```

**Resultado:**

```
ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-28 10:10:30.698295
id           : 3
titulo       : 1984

ano          : 1977
autor        : Clarice Lispector
data_criacao : 2026-07-28 10:10:59.597062
id           : 15
titulo       : A Hora da Estrela

ano          : 1945
autor        : George Orwell
data_criacao : 2026-07-28 10:10:59.446706
id           : 8
titulo       : A Revolução dos Bichos

ano          : 1937
autor        : Jorge Amado
data_criacao : 2026-07-28 10:10:59.560162
id           : 13
titulo       : Capitães da Areia

ano          : 2026
autor        : 3A1
data_criacao : 2026-07-28 10:10:30.698283
id           : 1
titulo       : Cotemig

ano          : 2026
autor        : 3A1
data_criacao : 2026-07-28 10:10:59.494213
id           : 10
titulo       : Cotemig

ano          : 1956
autor        : Guimarães Rosa
data_criacao : 2026-07-28 10:10:59.536666
id           : 12
titulo       : Grande Sertão: Veredas

ano          : 1865
autor        : José de Alencar
data_criacao : 2026-07-28 10:10:59.630913
id           : 17
titulo       : Iracema

ano          : 1928
autor        : Mário de Andrade
data_criacao : 2026-07-28 10:10:59.648227
id           : 18
titulo       : Macunaíma

ano          : 1881
autor        : Machado de Assis
data_criacao : 2026-07-28 10:10:59.517262
id           : 11
titulo       : Memórias Póstumas de Brás Cubas

ano          : 1988
autor        : Paulo Coelho
data_criacao : 2026-07-28 10:10:59.341094
id           : 4
titulo       : O Alquimista

ano          : 1955
autor        : Ariano Suassuna
data_criacao : 2026-07-28 10:10:59.612616
id           : 16
titulo       : O Auto da Compadecida

ano          : 1890
autor        : Aluísio Azevedo
data_criacao : 2026-07-28 10:10:30.698293
id           : 2
titulo       : O Cortiço

ano          : 1943
autor        : Antoine de Saint-Exupéry
data_criacao : 2026-07-28 10:10:59.470523
id           : 9
titulo       : O Pequeno Príncipe

ano          : 1938
autor        : Graciliano Ramos
data_criacao : 2026-07-28 10:10:59.579322
id           : 14
titulo       : Vidas Secas
```

**Total: 15 livros** (18 - 3 deletados = 15)

---

## Resumo das Operações

| Operação | Método HTTP | Endpoint | Resultado |
|----------|-------------|----------|-----------|
| Inserir 15 livros | POST | `/api/livros` | 201 Created (15x) |
| Atualizar livro ID 1 | PUT | `/api/livros/1` | 200 OK |
| Listar todos | GET | `/api/livros` | 200 OK (18 livros) |
| Excluir ID 5 | DELETE | `/api/livros/5` | 204 No Content |
| Excluir ID 6 | DELETE | `/api/livros/6` | 204 No Content |
| Excluir ID 7 | DELETE | `/api/livros/7` | 204 No Content |
| Listar todos (final) | GET | `/api/livros` | 200 OK (15 livros) |
