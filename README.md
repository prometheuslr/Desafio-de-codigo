# Google Sheets API Integration

Este projeto consiste em duas partes: um script para interagir com a API do Google Sheets (`googleSheets.py`) e um script principal (`main.py`) que utiliza a funcionalidade do primeiro para processar dados de uma planilha do Google Sheets.

## `googleSheets.py`

Este arquivo contém duas funções principais:

1. `sheets()`: Esta função se conecta à API do Google Sheets, autentica as credenciais e recupera os dados de uma planilha específica. Os dados são retornados como uma lista de listas, onde cada lista representa uma linha da planilha.

2. `upDateSheets(status, finalGrade)`: Esta função recebe duas listas, `status` e `finalGrade`, que contêm os status e as notas finais dos alunos, respectivamente. Ela então atualiza uma planilha do Google Sheets com essas informações.

Certifique-se de configurar corretamente o arquivo `client_secret.json` e `token.json` com as credenciais adequadas para autenticação com a API do Google Sheets.

## `main.py`

Este arquivo é o ponto de entrada principal do projeto. Ele utiliza as funções definidas em `googleSheets.py` para carregar os dados da planilha, calcular os status e as notas finais dos alunos e, em seguida, atualizar a planilha com essas informações.

## Configuração e Execução

1. Clone este repositório:
   - https://github.com/prometheuslr/Desafio-de-codigo.git


2. Instale as dependências necessárias:
   - pip install pandas google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

3. Configure as credenciais do Google Sheets:

   - Coloque o arquivo `client_secret.json` na raiz do projeto.
   - Após a primeira execução, o script irá solicitar que você faça login em sua conta do Google e autorize o acesso à planilha. Após autorizar, o arquivo `token.json` será gerado automaticamente para armazenar suas credenciais de acesso.

4. Execute o script principal:
   - python main.py

Isso irá processar os dados da planilha, calcular os status e as notas finais dos alunos e atualizar a planilha com essas informações.

Se precisar de mais alguma informação ou assistência, sinta-se à vontade para entrar em contato!