# Complementizer

O Complementizer facilita a criação e preenchimento de formulários automatizados para interações com APIs.

## 1. Complementizer Class

- **`Complementizer`** é uma classe que se conecta a uma API e autentica o usuário. Se a API requer um token de autenticação, ela faz uma requisição para obter o token e o armazena.

  - **Atributos principais:**
    - `url_base`: URL base da API.
    - `username` e `password`: Credenciais de autenticação.
    - `has_token` e `path_auth`: Determina se a autenticação requer um token e o caminho da autenticação.

  - **Método `populate`**:
    - Este método envia uma requisição POST para um endpoint específico, utilizando os dados gerados a partir de um formulário (`Form`). Ele imprime os dados gerados e a resposta da API.

## 2. Form Class

- **`Form`** é uma classe que representa um formulário vinculado a uma tabela específica. Ela utiliza a biblioteca `Faker` para gerar dados fictícios (como nomes, endereços, etc.) conforme o tipo do campo (`TypeField`).

  - **Método `createField`**:
    - Cria um campo no formulário com base no tipo (`TypeField`) e outros parâmetros opcionais (`info`). O método retorna o campo criado.
  
  - **Método `createDefault`**:
    - Cria um campo com valor padrão que não depende de geração de dados fictícios.
  
  - **Método `createDependency`**:
    - Cria uma dependência que busca dados a partir de uma API e armazena os valores possíveis.

  - **Método `generate`**:
    - Gera um dicionário com os dados de todos os campos, padrões e dependências do formulário.

## 3. Field Class

- **`Field`** representa um campo no formulário, como `nome_completo`, `cpf`, `data_nascimento`, etc. A classe utiliza a biblioteca `Faker` para gerar valores para esses campos dependendo do tipo (`TypeField`).

  - **Construtor**:
    - O campo é inicializado com um nome, tipo e um valor gerado automaticamente pelo `Faker`, dependendo do tipo do campo (ex.: nome, endereço, CPF, etc.).

## 4. TypeField Enum

- **`TypeField`** é um enumerador que define os diferentes tipos de campos que podem ser gerados no formulário, como `NAME_FULL`, `ADDRESS`, `DATE_OF_BIRTH`, `CPF`, etc.

## 5. Uso do Complementizer

No código principal:

- **Instância de `Complementizer`**:
  - Cria uma instância de `Complementizer` que conecta a uma API.

- **Laço `for`**:
  - Para cada iteração, cria um novo formulário (`Form`) para a tabela `participante`.
  - Adiciona diversos campos ao formulário, como `nome_completo`, `cpf`, `data_nascimento`, etc.
  - Usa a função `populate` para enviar os dados gerados para a API.

## Resumo

Este código é projetado para automatizar o preenchimento e envio de formulários para uma API. Ele facilita a criação de dados fictícios para testes, gerenciamento de dependências entre campos, e autenticação da API, tornando-o útil para cenários onde é necessário simular múltiplas submissões de formulários com dados variados.
