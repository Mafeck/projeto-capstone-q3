# HAKI API

HAKI API é uma aplicação que auxilia os profissionais da área jurídica na gestão de seus clientes.
Essa api permite que o advogado crie, altere e delete seu prórprio perfil; crie, atualize clientes, processos e comentários.



## Documentação da API

### As rotas abaixo não necessitam de autorização

#### ROTA USERS

#### Criar um perfil para o advogado

```http
  POST /api/users/register
```

Formato da requisição:

```js
  Body:
        {
            "cpf": "000.000.000-05",
            "oab": "0000000005",
            "name": "test 5",
            "last_name": "Matheus",
            "email": "test4@gmail.com",
            "password": "12345Aa@",
            "address": {
                "street": "street test 3",
                "number": "3",
                "district": "test 3",
                "state": "state Test 3",
                "country": "Country test 3",
                "cep": "800431-32"
            },
            "phone_number": [
                "00000000005"
            ]
        }
```

Formato da resposta: 201 CREATED

```js
  Body:
        {
          "oab": "0000000005",
          "name": "Advogada",
          "last_name": "Importante",
          "email": "adv1@mail.com.br",
          "address": {
            "street": "Tio de açis",
            "number": "420",
            "district": "test",
            "state": "Ceare",
            "country": "Brasil",
            "cep": "800431-32"
          },
          "phone_number": [
            {
              "phone": "00000000005"
            }
          ]
        }
```

**Possíveis Erros**
- Chave faltando: 400 BAD REQUEST
```js
    {
      "error": "Key 'oab' is missing."
    }
``` 
- Tipo de dado errado: 400 BAD REQUEST
```js
    {
      "error": "'oab', 'name' and 'last_name' must be a string type."
    }
```
- Usuário já existe: 400 BAD REQUEST
```js
    {
      "error": "Something went wrong"
    }
```  
- CPF formato errado: 400 BAD REQUEST
```js
    {
      "error": "CPF format is not valid. CPF must be like xxx.xxx.xxx-xx"
    }
```  
- E-mail formato errado: 400 BAD REQUEST
```js
    {
      "error": "email key must be an email type like 'person@client.com'"
    }
```  

----
----

#### Login da conta do advogado

```http
  POST /api/users/login
```

Formato da requisição:
```js
  Body:
        {
            "email": "test4@gmail.com",
            "password": "12345Aa@"
        }
```

Formato da resposta: 200 OK
```js
  Body:
        {
          "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0Njk3MDQzMiwianRpIjoiZjc1ZjM4YmItYTcyYi00MzRjLTgwODQtZDdhYjlhOTE4ZDZmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJvYWIiOiIxMjQ0NDU2IiwibmFtZSI6IkFkdm9nYWRhIiwibGFzdF9uYW1lIjoiSW1wb3J0YW50ZSIsImNwZiI6Ijk5OS4xMzAuNjc2LTIyIiwiZW1haWwiOiJhZHZAbWFpbC5jb20uYnIiLCJhZGRyZXNzX2lkIjoyLCJhZGRyZXNzIjp7InN0cmVldCI6IlRpbyBkZSBhXHUwMGU3aXMiLCJudW1iZXIiOiI0MjAiLCJkaXN0cmljdCI6InRlc3QiLCJzdGF0ZSI6IkNlYXJlIiwiY291bnRyeSI6IkJyYXNpbCIsImNlcCI6IjgwMDQzMS0zMiJ9fSwibmJmIjoxNjQ2OTcwNDMyLCJleHAiOjE2NDY5NzEzMzJ9.3-GgQxbHBvjn9mwcMQfZIWbGTF4K3yVziZXAikNe9Kc"
        }
```

**Possíveis erros:**
- E-mail ou senha errados: 400 BAD REQUEST
```js
      {
        "error": "email or password not match"
      }
``` 
- Chave faltando: 400 BAD REQUEST
```js
    {
      "error": "Key 'pasword' is missing."
    }
```  

----
----

### As rotas abaixo necessitam de autorização

Rotas que necessitam de autorização deve ser informado no cabeçalho da requisição o campo "Authorization", dessa forma:

Authorization: Bearer {token}


#### Pegar informações do advogado

```http
  GET /api/users
```

Formato da requisição:

```js
  Body: null      
```

Formato da resposta: 200 OK

```js
  Body:
        {
          "oab": "1244456",
          "name": "Advogada",
          "last_name": "Importante",
          "cpf": "999.130.676-22",
          "email": "adv@mail.com.br",
          "address_id": 2,
          "address": {
            "street": "Tio de açis",
            "number": "420",
            "district": "test",
            "state": "Ceare",
            "country": "Brasil",
            "cep": "800431-32"
        }
```

----
----

#### Atualizar informações do advogado

```http
  PATCH /api/users
```

Formato da requisição:
```js
  Body:
        {
          "name": "test 5",
          "last_name": "Matheus",
          "email": "test4@gmail.com",
          "password": "12345Aa@",
          "address": {
            "street": "street test 3",
            "number": "3",
            "district": "test 3",
            "state": "state Test 3",
            "country": "Country test 3",
            "cep": "800431-32"
          },
          "phone_number": [
            "00000000005"
          ]
        }
```

Formato da resposta: 200 OK

```js
  Body:
        {
          "oab": "1244456",
          "name": "Advogada",
          "last_name": "Importante",
          "cpf": "999.130.676-22",
          "email": "adv@mail.com.br",
          "address_id": 2,
          "address": {
            "street": "Tio de açis",
            "number": "420",
            "district": "test",
            "state": "Ceare",
            "country": "Brasil",
            "cep": "800431-32"
        }
```

**Possíveis erros:**
- Chave faltando: 400 BAD REQUEST
```js
    {
      "error": "Key 'oab' is missing."
    }
``` 
- Tipo de dado errado: 400 BAD REQUEST
```js
    {
      "error": "'oab', 'name' and 'last_name' must be a string type."
    }
```
- CPF formato errado: 400 BAD REQUEST
```js
    {
      "error": "CPF format is not valid. CPF must be like xxx.xxx.xxx-xx"
    }
```  
- E-mail formato errado: 400 BAD REQUEST
```js
    {
      "error": "email key must be an email type like 'person@client.com'"
    }
```  

----
----

#### Remover conta do usuário

```http
  DELETE /api/users
```

Formato da requisição: 
```js
  Body: null
```

Formato da resposta: 200 OK
```js
  Body: null
```
----
----

#### ROTA CLIENTS

#### Criar um cliente

```http
  POST /api/clients/register
```

Formato da requisição:
```js
  Body: 
        {
          "cpf": "000.000.000-05",
          "name": "test3",
          "last_name": "Matheus",
          "email": "test5@gmail.com",
          "marital_status": "solteiro",
          "password": "12345Aa@",
          "address": {
            "street": "test 4",
            "number": "4",
            "district": "test 4",
            "state": "test 4",
            "country": "test 4",
            "cep": "800431-32"
          },
          "phone_number": [
            "00000000014"
          ]
        }
```

Formato da resposta: 200 OK

```js
  Body:
        {
          "cpf": "000.000.000-05",
          "name": "test3",
          "last_name": "Matheus",
          "email": "test5@gmail.com",
          "marital_status": "solteiro",
          "address": {
            "street": "test 4",
            "number": "4",
            "district": "test 4",
            "state": "test 4",
            "country": "test 4",
            "cep": "800431-32"
          }
        }
```

**Possíveis Erros**
- Chave faltando: 400 BAD REQUEST
```js
    {
      "error": "Key 'oab' is missing."
    }
``` 
- Tipo de dado errado: 400 BAD REQUEST
```js
    {
      "error": "'oab', 'name' and 'last_name' must be a string type."
    }
```
- Cliente já existe: 400 BAD REQUEST
```js
    {
      "error": "Something went wrong"
    }
```  
- CPF formato errado: 400 BAD REQUEST
```js
    {
      "error": "CPF format is not valid. CPF must be like xxx.xxx.xxx-xx"
    }
```  
- E-mail formato errado: 400 BAD REQUEST
```js
    {
      "error": "email key must be an email type like 'person@client.com'"
    }
```  

----
----


#### Listar todos os clientes

```http
  GET /api/clients
```

Formato da requisição:
```js
  Body: null
```

Formato da resposta: 200 OK
```js
  Body:
        {
          "clients": [
            {
              "cpf": "000.000.000-05",
              "name": "test3",
              "last_name": "Matheus",
              "email": "test5@gmail.com",
              "marital_status": "solteiro",
              "address_id": 2,
              "address": {
                "street": "test 4",
                "number": "4",
                "district": "test 4",
                "state": "test 4",
                "country": "test 4",
                "cep": "800431-32"
              }
            }
          ]
        }
```

----
----

#### Listar as informações de um cliente específico

```http
  GET /api/clients/<client_cpf>
```

Formato da requisição:
```js
  Body: null
```

Formato da resposta: 200 OK
```js
  Body:
        {
          "cpf": "000.000.000-05",
          "name": "test3",
          "last_name": "Matheus",
          "email": "test5@gmail.com",
          "marital_status": "solteiro",
          "address_id": 2,
          "address": {
            "street": "test 4",
            "number": "4",
            "district": "test 4",
            "state": "test 4",
            "country": "test 4",
            "cep": "800431-32"
          }
        }
```

----
----


#### Atualizar informações do cliente

```http
  PATCH /api/clients/<client_cpf>
```

Formato da requisição:
```js
  Body: 
        {
          "cpf": "000.000.000-05",
          "last_name": "test",
          "email": "test3@gmail.com",
          "marital_status": "solteiro",
          "password": "12345Aa@"
        } 
```

Formato da resposta: 200 OK
```js
  Body:
        {
          "cpf": "000.000.000-05",
          "name": "test3",
          "last_name": "Matheus",
          "email": "test5@gmail.com",
          "marital_status": "solteiro",
          "address_id": 2,
          "address": {
            "street": "test 4",
            "number": "4",
            "district": "test 4",
            "state": "test 4",
            "country": "test 4",
            "cep": "800431-32"
          }
        }
```

**Possíveis Erros**
- Chave faltando: 400 BAD REQUEST
```js
    {
      "error": "Key 'oab' is missing."
    }
``` 
- Tipo de dado errado: 400 BAD REQUEST
```js
    {
      "error": "'oab', 'name' and 'last_name' must be a string type."
    }
```
- Cliente já existe: 400 BAD REQUEST
```js
    {
      "error": "Something went wrong"
    }
```  
- CPF formato errado: 400 BAD REQUEST
```js
    {
      "error": "CPF format is not valid. CPF must be like xxx.xxx.xxx-xx"
    }
```  
- E-mail formato errado: 400 BAD REQUEST
```js
    {
      "error": "email key must be an email type like 'person@client.com'"
    }
```  
- Cliente não cadastrado: 404 NOT FOUND
```js
      {
        "error": "Client not found"
      }
```

----
----

#### Remover cliente

```http
  DELETE /api/clients/<client_cpf>
```

Formato da requisição:
```js
  Body: null
```

Formato da resposta: 204 NO CONTENT
```js
  Body: null
```

**Possíveis erros**
- Cliente não cadastrado: 404 NOT FOUND
```js
      {
        "error": "Client not found"
      }
```

----
----


#### ROTA COMMENTS

#### Criar um comentário

```http
  POST /api/clients/comments
```

Formato da requisição:
```js
  Body: 
        {
          "comment": "First comment",
          "clients_cpf": [
          "000.000.000-29",
          "000.000.000-28"	
          ]
        }
```

Formato da resposta: 200 OK
```js
  Body: 
        {
          "message": {
            "comment": "First comment",
            "created_at": "Wed, 09 Mar 2022 23:58:45 GMT",
            "clients": [
              {
                "cpf": "000.000.000-29",
                "name": "Cliente",
                "last_name": "Matheus",
                "email": "testCli@gmail.com",
                "marital_status": "solteiro",
                "address_id": 1,
                "address": {
                  "street": "Mãe de açis",
                  "number": "423",
                  "district": "test",
                  "state": "Ceare",
                  "country": "Brasil",
                  "cep": "800431-32"
                }
              },
              {
                "cpf": "000.000.000-28",
                "name": "Cliente",
                "last_name": "Matheus",
                "email": "testCli11@gmail.com",
                "marital_status": "solteiro",
                "address_id": 1,
                "address": {
                  "street": "Mãe de açis",
                  "number": "423",
                  "district": "test",
                  "state": "Ceare",
                  "country": "Brasil",
                  "cep": "800431-32"
                }
              }
            ]
          }
        }        
```

----
----


#### Listar todos os comentários por CPF

```http
  GET /api/clients/comments/<client_cpf>
```

Formato da requisição:
```js
  Body: null
```

Formato da requisição: 200 OK
```js
  Body:
        {
          "comments": []
        }
```

**Possíveis erros**
- Cliente não cadastrado: 404 NOT FOUND
```js
      {
        "error": "Client not found"
      }
```

----
----

#### LListar todos os comentários por ID

```http
  GET /api/clients/comments?client_cpf=<cpf>&comment_id=<id>
```

Formato da requisição:
```js
  Body: null
```
Formato da resposta: 200 OK
```js
      {
        "id": 4,
        "comment": "First comment",
        "create_date": "Fri, 11 Mar 2022 03:39:34 GMT",
        "update_at": "Fri, 11 Mar 2022 03:39:34 GMT" 
      }
```

**Possíveis erros**
- Cliente não cadastrado: 404 NOT FOUND
```js
      {
        "error": "Client not found"
      }
```
- Comentário não cadastrado: 404 NOT FOUND
```js
      {
        "error": "Comment not found"
      }
```

----
----

#### Atualizar informações do comentários
*A chave "title" é opcional.

```http
  PATCH /api/clients/comments/<comment_id>
```

Formato da requisição:
```js
  Body: 
        {
          "title": "New Title"
          "comment": "Update comment 0.2"
        }
```

Formato da resposta: 200 OK
```js
  Body: null
```

----
----

#### Remover comentário

```http
  DELETE /api/clients/comments/<comment_id>
```

Formato da requisição:
```js
  Body: 
        {
          "client_cpf": "000.000.000-07"
        }
```

Formato da resposta: 200 OK
```js
  Body: null
```

----
----

#### ROTA PROCESSES

#### Criar um processo

```http
  POST /api/clients/processes
```

Formato da requisição:
```js
  Body: 
        {
          "number": "123456",
          "description": "eae 22"
        }
```
Formato da resposta: 201 CREATED
```js
  Body: 
        {
          "number": "1214156",
          "description": "eae 22"
        }
```

**Possíveis erros**
- Chave/dado passado errado 400 BAD REQUEST
```js
      {
        "error": "Something went wrong"
      }
```
- Chave faltando: 400 BAD REQUEST
```js
    {
      "error": "Key 'description' is missing."
    }
``` 

----
----

#### Listar todos os processos de um cliente

```http
  GET /api/clients/processes/<cpf>
```

Formato da requisição:
```js
  Body: null
```
Formato da resposta: 200 OK
```js
  Body: 
        {
          "processes":
                  [
                    {
                      "number": "123456",
                      "description": "eae 22"
                    },
                    {
                      "number": "1234156",
                      "description": "eae 22"
                    },
                    {
                      "number": "1214156",
                      "description": "eae 22"
                    }
                  ]
        }
```

----
----


#### Listar um processo específico do cliente
```http
  GET /api/clients/processes?number_process=<process_number>&client_cpf=<cpf>
```

Formato da requisição:
```js
  Body: null
```
Formato da resposta: 200 OK
```js
  Body: 
        {
          "number": "55677567",
          "description": "testando processes 0.2"
        }
```

Formato da resposta: 200 OK
```js
  Body: null
```

----
----

#### Listar o processos de todos os clientes do advogado
```http
  GET /api/clients/processes/
```

Formato da requisição:
```js
  Body: null
```
Formato da resposta: 200 OK
```js
  Body: null
```

Formato da resposta: 200 OK
```js
  Body: {
           "processes": {
                         "number": "55677567",
                         "description": "testando processes 0.2"
                        }
        }
```

----
----

#### Atualizar informações do processo

```http
  PATCH /api/clients/processos/<process_id>
```

Formato da requisição:
```js
  Body: 
        {
          "description": "eae 22"
        }
```
Formato da resposta: 200 OK
```js
  Body: null
```

**Possíveis Erros**
- Processo não existe: 404 NOT FOUND
```js
      {
        "message": "Process not found"
      }
```

----
----


#### Remover comentário

```http
  DELETE /api/clients/comments/<comment_id>
```

Formato da requisição:
```js
  Body: 
        {
          "client_cpf": "000.000.000-07"
        }
```