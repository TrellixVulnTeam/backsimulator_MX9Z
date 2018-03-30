#WebService

*
* [User](#user)
  * [Adicionar User](#adicionar-user)
  * [Listar todos os Users](#listar-todos-os-users)
  * [Buscar um User](#buscar-um-user)
  * [Editar um User](#editar-um-user)
  * [Deletar um User](#deletar-um-user) 

  `


## User
Responsável pelas informações dos Users cadastrados no sistema.

### Adicionar User
Responsável pela adição de um determinado User.

```http
POST /user HTTP/1.1
```

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|nome|String|-|-|-|Não|Nome do User.|
|email|String|-|-|-|Não|Email do User.|
|password|String|-|-|-|Não|Password do User.|
|img|String|-|-|-|Não|Imagem do User.|
|admin|Boolean|-|-|-|Não|Caso o User seja Administrador do Sistema.|


**Requisição:**
```http
POST /user HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
  "name": "user",
  "email": "asdas",
  "password": "$2a$10$gTNEE5O1qP3QdBEKoILxuuHiekWaZ8WI/mr.euWd/03CJQTSAjkjG",
  "img": "///",
  "admin": true
}

```

**Resposta:**

```http
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: xxx
Location: /user/507f1f77bcf86cd799439011
```

### Listar todos os Users

```http
GET /user HTTP/1.1
```

Retorna todos os Users.

**Requisição:**

```http
GET /user HTTP/1.1
```

**Resposta:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: xxx
```
```json
{
  "Error": false,
  "Data": [
        {
            "_id": "59095bab99f2270a6c86284d",
            "name": "user",
            "email": "asdas",
            "password": "$2a$10$gTNEE5O1qP3QdBEKoILxuuHiekWaZ8WI/mr.euWd/03CJQTSAjkjG",
            "img": "///",
            "admin": true,
            "__v": 0
        },
        {
            "_id": "5909640333a0a7117293d253",
            "name": "se",
            "password": "$2a$10$sbw6tWhNsqfUcZkmdaue9u.WblipukaeEkbmZgvzBKyqgtDUbw.dm",
            "__v": 0
        }
  ]
}
```

### Buscar um User

```http
GET /user/{:id} HTTP/1.1
```

Retorna o registro do User cujo ID foi recebido.

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID do User a ser pesquisado.|

**Requisição:**

```http
GET /user/507f1f77bcf86cd799439011 HTTP/1.1
```

**Resposta:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: xxx
```
```json
{
    "Error": false,
    "data": {
        {
            "_id": "59095bab99f2270a6c86284d",
            "name": "user",
            "email": "asdas",
            "password": "$2a$10$gTNEE5O1qP3QdBEKoILxuuHiekWaZ8WI/mr.euWd/03CJQTSAjkjG",
            "img": "///",
            "admin": true,
            "__v": 0
        }
    }
}
```

### Editar um User

```http
PUT /user/{:id} HTTP/1.1
```

Faz a edição do registro do User.

**Observações:** *Passar somente os atributos que serão atualizados.*

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID do User passado na URL.|
|nome|String|-|-|-|Não|Nome do User.|
|email|String|-|-|-|Não|Email do User.|
|password|String|-|-|-|Não|Password do User.|
|img|String|-|-|-|Não|Imagem do User.|
|admin|Boolean|-|-|-|Não|Caso o User seja Administrador do Sistema.|

**Requisição:**

```http
PUT /user/507f1f77bcf86cd799439011 HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
   "name": "user"
}
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```

### Editar ou Adicionar atributo a um User

```http
PATCH /user/{:id} HTTP/1.1
``` 

Faz a edição de um atributo específico do User.

**Observações:** *Passar somente os atributos que serão atualizados.*

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID do User passado na URL.|
|nome|String|-|-|-|Não|Nome do User.|
|email|String|-|-|-|Não|Email do User.|
|password|String|-|-|-|Não|Password do User.|
|img|String|-|-|-|Não|Imagem do User.|
|admin|Boolean|-|-|-|Não|Caso o User seja Administrador do Sistema.|

**Requisição:**

```http
PUT /user/507f1f77bcf86cd799439011 HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
  "name": "user"
}
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```

### Deletar um User

```http
DELETE /user/{:id} HTTP/1.1
```
Remove o User com o ID passado.


**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID do User a ser removido.|

**Requisição:**

```http
DELETE /user/507f1f77bcf86cd799439011 HTTP/1.1
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```
