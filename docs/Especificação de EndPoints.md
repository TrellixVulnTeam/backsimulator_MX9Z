



Ecomaps
WebService
===

* [Árvore](#arvore)
  * [Adicionar Árvore](#adicionar-arvore)
  * [Listar todas as Árvores](#listar-todas-as-arvores)
  * [Buscar uma Árvore](#buscar-uma-arvore)
  * [Editar uma Árvore](#editar-uma-arvore)
  * [Editar ou Adicionar atributos a uma Árvore](#editar-ou-adicionar-atributos-a-uma-arvore)
  * [Deletar uma Árvore](#deletar-uma-arvore)
* [Fóssil](#fóssil)
  * [Adicionar Fóssil](#adicionar-fossil)
  * [Listar todos os Fósseis](#listar-todas-os-fosseis)
  * [Buscar um Fóssil](#buscar-um-fossil)
  * [Editar um Fóssil](#editar-um-fossil)
  * [Editar ou Adicionar atributos a um Fóssil](#editar-ou-adicionar-atributos-a-um-fossil)
  * [Deletar um Fóssil](#deletar-um-fossil)
 * [Inseto](#inseto)
    * [Adicionar Inseto](#adicionar-inseto)
    * [Listar todos os Insetos](#listar-todos-os-insetos)
    * [Buscar um Inseto](#buscar-um-inseto)
    * [Editar um Inseto](#editar-um-inseto)
    * [Editar ou Adicionar atributos a um Inseto](#editar-ou-adicionar-atributos-a-um-inseto)
    * [Deletar um Inseto](#deletar-um-inseto)
* [User](#user)
  * [Adicionar User](#adicionar-user)
  * [Listar todos os Users](#listar-todos-os-users)
  * [Buscar um User](#buscar-um-user)
  * [Editar um User](#editar-um-user)
  * [Editar ou Adicionar atributos a um User](#editar-ou-adicionar-atributos-a-um-user)
  * [Deletar um User](#deletar-um-user) 
* [História](#historia)
  * [Adicionar História](#adicionar-história)
  * [Listar todas as Histórias](#listar-todas-as-histórias)
  * [Buscar uma História](#buscar-uma-história)
  * [Editar uma História](#editar-uma-história)
  * [Editar ou Adicionar atributos a uma História](#editar-ou-adicionar-atributos-a-uma-história)
  * [Deletar uma História](#deletar-uma-história)
  
## <a name="arvore"></a> Árvore
Responsável pelas informações das Árvores cadastradas no sistema.

### <a name="adicionar-arvore"></a> Adicionar Árvore
Responsável pela adição de uma determinada árvore.

```http
POST /trees HTTP/1.1
```

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|nome_pop|String|-|-|-|Não|Nome popular da Árvore.|
|nome_cie|String|-|-|-|Não|Nome científico da Árvore.|
|familia|String|-|-|-|Não|Família da Árvore.|
|categoria|String|-|-|-|Não|Categoria da Árvore.|
|origem|String|-|-|-|Não|Origem da Árvore.|
|clima|String|-|-|-|Não|Clima da Árvore.|
|luminosidade|String|-|-|-|Não|Luminosidade da Árvore.|
|altura|String|-|-|-|Não|Altura da Árvore.|
|info|String|-|-|-|Não|Informações da Árvore.|
|localidade|String|-|-|-|Não|Localidade da Árvore.|
|loc|Array.JSON|-|-|-|Não|Coordenadas da Árvore.|
|loc.lat|Numeric|-|-|-|Não|Latitude onde a Árvore se encontra no mapa.|
|loc.lng|Numeric|-|-|-|Não|Longitude onde a Árvore se encontra no mapa.|

**Requisição:**
```http
POST /trees HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
            "nome_pop": "Munguba, Cacau-selvagem, Castanheira-da-água, Castanheiro-de-guiana, Castanheiro-do-maranhão, Falso-cacau, Mamorana, Monguba, Mungaba",
            "nome_cie": "Pachira aquática",
            "familia": "Bombacaceae",
            "categoria": "Árvores, Árvores Frutíferas, Árvores Ornamentais",
            "origem": "América Central, América do Sul",
            "clima": "Equatorial, Subtropical, Tropical",
            "luminosidade": "Sol Pleno",
            "altura": "3.0 a 3.6 metros, 3.6 a 4.7 metros, 4.7 a 6.0 metros, 6.0 a 9.0 metros, 9.0 a 12 metros, acima de 12 metros",
            "info": "A monguba é uma bela árvore tropical, de caule frondoso e copa arredondada, capaz de alcançar 18 metros de altura.",
            "loc": [
                {
                    "lat": -7.20523888,
                    "lng": -39.44765115
                }
            ]
        }
```

**Resposta:**

```http
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: xxx
Location: /trees/507f1f77bcf86cd799439011
```

### Listar todas as Árvores

```http
GET /trees HTTP/1.1
```

Retorna todas as Árvores.

**Requisição:**

```http
GET /trees HTTP/1.1
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
      "_id": "59ee3ab7fadb5e001169642a",
      "categoria": ".",
      "luminosidade": ".",
      "familia": "Fabaceae-Faboideae",
      "origem": ".",
      "clima": ".",
      "info": ".",
      "altura": ".",
      "nome_cie": "Andira cordata Arroyo ex R.T. Penn. & H. C. Lima",
      "__v": 0,
      "loc": [],
      "nome_pop": "Amargoso"
    },
    {
            "_id": "58f6768c7bb5070011d6e922",
            "nome_pop": "Munguba, Cacau-selvagem, Castanheira-da-água, Castanheiro-de-guiana, Castanheiro-do-maranhão, Falso-cacau, Mamorana, Monguba, Mungaba",
            "nome_cie": "Pachira aquática",
            "familia": "Bombacaceae",
            "categoria": "Árvores, Árvores Frutíferas, Árvores Ornamentais",
            "origem": "América Central, América do Sul",
            "clima": "Equatorial, Subtropical, Tropical",
            "luminosidade": "Sol Pleno",
            "altura": "3.0 a 3.6 metros, 3.6 a 4.7 metros, 4.7 a 6.0 metros, 6.0 a 9.0 metros, 9.0 a 12 metros, acima de 12 metros",
            "info": "A monguba é uma bela árvore tropical, de caule frondoso e copa arredondada, capaz de alcançar 18 metros de altura.",
            "loc": [
                {
                    "_id": {
                        "$oid": "58f6768c7bb5070011d6e923"
                    }
                },
                {
                    "lat": -7.20523888,
                    "lng": -39.44765115
                }
            ],
            "__v": 0
        }
  ]
}
```

###<a name="buscar-uma-arvore"></a> Buscar uma Árvore

```http
GET /trees/{:id} HTTP/1.1
```

Retorna o registro da Árvore cujo ID foi recebido.

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID da Árvore a ser pesquisada.|

**Requisição:**

```http
GET /trees/507f1f77bcf86cd799439011 HTTP/1.1
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
        "_id": "58f6768c7bb5070011d6e922",
        "nome_pop": "Munguba, Cacau-selvagem, Castanheira-da-água, Castanheiro-de-guiana, Castanheiro-do-maranhão, Falso-cacau, Mamorana, Monguba, Mungaba",
        "nome_cie": "Pachira aquática",
        "familia": "Bombacaceae",
        "categoria": "Árvores, Árvores Frutíferas, Árvores Ornamentais",
        "origem": "América Central, América do Sul",
        "clima": "Equatorial, Subtropical, Tropical",
        "luminosidade": "Sol Pleno",
        "altura": "3.0 a 3.6 metros, 3.6 a 4.7 metros, 4.7 a 6.0 metros, 6.0 a 9.0 metros, 9.0 a 12 metros, acima de 12 metros",
        "info": "A monguba é uma bela árvore tropical, de caule frondoso e copa arredondada, capaz de alcançar 18 metros de altura. Nas florestas tropicais podemos encontrá-la em ambientes brejosos, ou à margem de rios e lagos, o nome científico “aquatica” provém desta característica. Apresenta folhas grandes e palmadas, dividas em 6 a 9 folíolos verdes e brilhantes. As flores são muito bonitas e perfumadas, com longos estames de extremidade rosada e base amarela. Os frutos grandes e compridos, semelhantes ao cacau, contém paina sedosa e branca que envolve as sementes. As sementes da monguba podem ser consumidas torradas, fritas ou assadas, e até trituradas como um sucedâneo do café ou chocolate, e diz-se que são muito saborosas. Adapta-se a um ampla faixa climática, desde o calor equatorial até o frio subtropical. A falta de luminosidade acarreta o amarelamento das folhas. Multiplica-se por estaquia ou sementes.",
        "loc": [
            {
                "_id": {
                    "$oid": "58f6768c7bb5070011d6e923"
                }
            },
            {
                "lat": -7.20523888,
                "lng": -39.44765115
            }
        ],
        "__v": 0
    }
}
```

###<a name="editar-uma-arvore"></a> Editar uma Árvore

```http
PUT /trees/{:id} HTTP/1.1
```

Faz a edição do registro da Árvore.

**Observações:** *Passar somente os atributos que serão atualizados.*

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID da Árvore passado na URL.|
|nome_pop|String|-|-|-|Não|Nome popular da Árvore.|
|nome_cie|String|-|-|-|Não|Nome científico da Árvore.|
|familia|String|-|-|-|Não|Família da Árvore.|
|categoria|String|-|-|-|Não|Categoria da Árvore.|
|origem|String|-|-|-|Não|Origem da Árvore.|
|clima|String|-|-|-|Não|Clima da Árvore.|
|luminosidade|String|-|-|-|Não|Luminosidade da Árvore.|
|altura|String|-|-|-|Não|Altura da Árvore.|
|info|String|-|-|-|Não|Informações da Árvore.|
|localidade|String|-|-|-|Não|Localidade da Árvore.|
|loc|Array.JSON|-|-|-|Não|Coordenadas da Árvore.|
|loc.lat|Numeric|-|-|-|Não|Latitude onde a Árvore se encontra no mapa.|
|loc.lng|Numeric|-|-|-|Não|Longitude onde a Árvore se encontra no mapa.|

**Requisição:**

```http
PUT /trees/507f1f77bcf86cd799439011 HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
   "origem": "América Central, América do Sul"
}
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```

###<a name="editar-ou-adicionar-atributo-a-uma-arvore"></a> Editar ou Adicionar atributo a uma Árvore

```http
PATCH /trees/{:id} HTTP/1.1
``` 

Faz a edição de um atributo específico da Árvore.

**Observações:** *Passar somente os atributos que serão atualizados.*

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID da Árvore passado na URL.|
|nome_pop|String|-|-|-|Não|Nome popular da Árvore.|
|nome_cie|String|-|-|-|Não|Nome científico da Árvore.|
|familia|String|-|-|-|Não|Família da Árvore.|
|categoria|String|-|-|-|Não|Categoria da Árvore.|
|origem|String|-|-|-|Não|Origem da Árvore.|
|clima|String|-|-|-|Não|Clima da Árvore.|
|luminosidade|String|-|-|-|Não|Luminosidade da Árvore.|
|altura|String|-|-|-|Não|Altura da Árvore.|
|info|String|-|-|-|Não|Informações da Árvore.|
|localidade|String|-|-|-|Não|Localidade da Árvore.|
|loc|Array.JSON|-|-|-|Não|Coordenadas da Árvore.|
|loc.lat|Numeric|-|-|-|Não|Latitude onde a Árvore se encontra no mapa.|
|loc.lng|Numeric|-|-|-|Não|Longitude onde a Árvore se encontra no mapa.|

**Requisição:**

```http
PUT /trees/507f1f77bcf86cd799439011 HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
  "origem": "América Central, América do Sul"
}
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```

### Deletar uma Árvore

```http
DELETE /trees/{:id} HTTP/1.1
```
Remove a Árvore com o ID passado.


**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID da Árvore a ser removida.|

**Requisição:**

```http
DELETE /trees/507f1f77bcf86cd799439011 HTTP/1.1
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```


## Fóssil
Responsável pelas informações dos Fósseis cadastrados no sistema.

### Adicionar Fóssil
Responsável pela adição de um determinado Fóssil.

```http
POST /fosseis HTTP/1.1
```

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|fossil|Boolean|-|-|-|Não|Caso seja um Fóssil.|
|designacao|String|-|-|-|Não|Designação do Fóssil.|
|estratigrafia|String|-|-|-|Não|Estratigrafia do Fóssil.|
|idade|String|-|-|-|Não|Idade do Fóssil.|
|procedencia|String|-|-|-|Não|Procedencia do Fóssil.|
|info|String|-|-|-|Não|Informações do Fóssil.|


**Requisição:**
```http
POST /fosseis HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
  "idade": "Cretáceo",
  "procedencia": "Chapada do Araripe",
  "estratigrafia": "Formação  Crato",
  "designacao": "Brachyphyllum obesum",
  "info": "GIMNOSPERMA - Coníferas Fonte: Guia para trabalhos de campo. FEITOSA et al. (2013)",
  "fossil": true
}
```

**Resposta:**

```http
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: xxx
Location: /fosseis/507f1f77bcf86cd799439011
```

###<a name="listar-todos-os-fosseis"></a> Listar todos os Fósseis

```http
GET /fosseis HTTP/1.1
```

Retorna todos os Fósseis.

**Requisição:**

```http
GET /fosseis HTTP/1.1
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
            "_id": "5a25d2ef6132ff0a62d50ae8",
            "idade": "Cretáceo",
            "procedencia": "Chapada do Araripe",
            "estratigrafia": "Formações Crato, Ipubi e Romualdo",
            "designacao": "Tharrhias araripis",
            "info": "Sobre o Tharrhias da Chapada do Araripe\" tem por finalidade uma melhor compreensão da ictiofáunula do cretáceo da Chapada do Araripe, no nordeste do Brasil. O gênero Tharrhias é reestudado dando-se a definida diagnose e esclarecendo a sua posição taxonômica entre os Chianidae e a interrelação com os demais gênros dessa família, especialmente as formas\nfósseis do Cretáceo. O problema da validade das espécies, Tharrhias araripis JORDAN & BRANNER, (1908) e Tharrhias rochae (JORDAN & BRANNER,1908) é analisado, após o estudo das mesmas, baseado em material das coleções paleoictiológicas do DNPM. Ambas as espécies são consideradas válidas do ponto de vista taxonômico sendo redescritas e recebendo nova caracterização. Num exame das condições de deposição dos sedimentos da Chapada do Araripe, focalizou o sistema de vida que possivelmente tiveram esses Chianidae do Cretáceo do Araripe e a razão do número elevado de fósseis desses peixes entre os ictiólitos encontrados nos sedimentos da Formação Santana. (OLIVEIRA, Anuário IGeo capa > v. 16, 1993)  Designação: Álamo Feitosa Saraiva (2017).",
            "fossil": true
        },
        {
            "_id": "5a399f7f6132ff0a62d50afb",
            "idade": "Cretáceo",
            "procedencia": "Chapada do Araripe",
            "estratigrafia": "Formação Crato",
            "designacao": "Ararpegryllus serrilhatus",
            "info": "Ordem: Ensifera - Grilo.\nFonte: Guia para trabalhos de campo. FEITOSA et al. (2013)",
            "fossil": true
        },
        {
            "_id": "5a39a0f76132ff0a62d50afd",
            "idade": "Cretáceo",
            "procedencia": "Chapada do Araripe",
            "estratigrafia": "Formação  Crato",
            "designacao": "Brachyphyllum obesum",
            "info": "GIMNOSPERMA - Coníferas\nFonte: Guia para trabalhos de campo. FEITOSA et al. (2013)",
            "fossil": true
        }
  ]
}
```

### Buscar um Fóssil

```http
GET /fosseis/{:id} HTTP/1.1
```

Retorna o registro do Fóssil cujo ID foi recebido.

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID do Fóssil a ser pesquisado.|

**Requisição:**

```http
GET /fosseis/507f1f77bcf86cd799439011 HTTP/1.1
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
            "_id": "5a399f7f6132ff0a62d50afb",
            "idade": "Cretáceo",
            "procedencia": "Chapada do Araripe",
            "estratigrafia": "Formação Crato",
            "designacao": "Ararpegryllus serrilhatus",
            "info": "Ordem: Ensifera - Grilo.\nFonte: Guia para trabalhos de campo. FEITOSA et al. (2013)",
            "fossil": true
        }
    }
}
```

### Editar um Fóssil

```http
PUT /fosseis/{:id} HTTP/1.1
```

Faz a edição do registro do Fóssil.

**Observações:** *Passar somente os atributos que serão atualizados.*

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID do Fóssil passado na URL.|
|fossil|Boolean|-|-|-|Não|Caso seja um Fóssil.|
|designacao|String|-|-|-|Não|Designação do Fóssil.|
|estratigrafia|String|-|-|-|Não|Estratigrafia do Fóssil.|
|idade|String|-|-|-|Não|Idade do Fóssil.|
|procedencia|String|-|-|-|Não|Procedencia do Fóssil.|
|info|String|-|-|-|Não|Informações do Fóssil.|

**Requisição:**

```http
PUT /fosseis/507f1f77bcf86cd799439011 HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
   "procedencia": "Chapada do Araripe"
}
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```

### Editar ou Adicionar atributo a um Fóssil

```http
PATCH /fosseis/{:id} HTTP/1.1
``` 

Faz a edição de um atributo específico do Fóssil.

**Observações:** *Passar somente os atributos que serão atualizados.*

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID do Fóssil passado na URL.|
|fossil|Boolean|-|-|-|Não|Caso seja um Fóssil.|
|designacao|String|-|-|-|Não|Designação do Fóssil.|
|estratigrafia|String|-|-|-|Não|Estratigrafia do Fóssil.|
|idade|String|-|-|-|Não|Idade do Fóssil.|
|procedencia|String|-|-|-|Não|Procedencia do Fóssil.|
|info|String|-|-|-|Não|Informações do Fóssil.|

**Requisição:**

```http
PUT /fosseis/507f1f77bcf86cd799439011 HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
  "procedencia": "Chapada do Araripe"
}
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```

### Deletar um Fóssil

```http
DELETE /fosseis/{:id} HTTP/1.1
```
Remove o Fóssil com o ID passado.


**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID do Fóssil a ser removido.|

**Requisição:**

```http
DELETE /fosseis/507f1f77bcf86cd799439011 HTTP/1.1
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```

* [Inseto](#inseto)
  * [Adicionar Inseto](#adicionar-inseto)
  * [Listar todos os Insetos](#listar-todas-as-insetos)
  * [Buscar um Inseto](#buscar-um-inseto)
  * [Editar um Inseto](#editar-um-inseto)
  * [Editar ou Adicionar atributos a um Inseto](#editar-ou-adicionar-atributos-a-um-inseto)
  * [Deletar um Inseto](#deletar-um-inseto)

## Inseto
Responsável pelas informações dos Insetos cadastrados no sistema.

### Adicionar Inseto
Responsável pela adição de um determinado Inseto.

```http
POST /insetos HTTP/1.1
```

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|inseto|Boolean|-|-|-|Não|Caso seja um Inseto.|
|ordem|String|-|-|-|Não|Ordem do Inseto.|
|reino|String|-|-|-|Não|Reino do Inseto.|
|filo|String|-|-|-|Não|Filo do Inseto.|
|classe|String|-|-|-|Não|Classe do Inseto.|
|info|String|-|-|-|Não|Informações do Inseto.|


**Requisição:**
```http
POST /insetos HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
  "info": "São agrupados nessa ordem os gafanhotos, as esperanças, os grilos, as paquinhas e as taquarinhas. Esses insetos possuem o terceiro par de perna do tipo saltatório. Cabeça muito variável quanto à forma. Muitas espécies apresentam cabeça consideravelmente prolongada entre os olhos. Possuem antenas filiformes. O aparelho bucal é mastigador. As fêmeas podem apresentar ovopositor longo com aspectos de laminas. Pernas anteriores e medianas ambulatórias, nas paquinhas o par anterior é fossorial. Na maioria das espécies há dois pares de asas, sendo o anterior do tipo tégmina e o posterior membranoso. A maioria dos orthopteros apresentam tímpanos (órgãos auditivos) localizados de cada lado de cada do primeiro urômetro.",
            "ordem": "Orthoptera",
            "filo": "Arthropoda",
            "classe": "Insecta",
            "reino": "Animalia",
            "inseto": true
}
```

**Resposta:**

```http
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: xxx
Location: /insetos/507f1f77bcf86cd799439011
```

### Listar todos os Insetos

```http
GET /insetos HTTP/1.1
```

Retorna todos os Insetos.

**Requisição:**

```http
GET /insetos HTTP/1.1
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
            "_id": "5a25ccb26132ff0a62d50ade",
            "info": "A ordem hymenoptera é um dos maiores grupos de insetos que existe as vespas, abelhas, formigas. As fêmeas possuem ovopositor, o que permite a perfuração do hospedeiro e pode por muitas vezes estar modificado por um ferrão. Possuem olhos bastante desenvolvidos podendo ser por milhares de omatídeos. O aparelho bucal é do tipo lambedor (nas abelhas) e mastigador nos demais. Possuem quatro asas membranosas, onde as posteriores são maiores que as anteriores. Algumas são ápteras, isso vai depender da casta em que ela se encontra, como nas formigas. Se desenvolvem através de metamorfose completa. Insetos sociais, como os hymenópteros, trabalham juntos para realizar grandes tarefas. Como no caso das abelhas da espécie: Apis melífera, da família: apidae. Esta por sua vez é uma abelha social de origem europeia, seu habitat é bastante diversificado, inclui savanas, florestas tropicais, deserto, regiões litorâneas e montanhosas.",
            "ordem": "Hymenoptera ",
            "filo": "Arthropoda",
            "classe": "Insecta",
            "reino": "Animalia",
            "inseto": true
        },
        {
            "_id": "5a25cd076132ff0a62d50adf",
            "info": "São agrupados nessa ordem os gafanhotos, as esperanças, os grilos, as paquinhas e as taquarinhas. Esses insetos possuem o terceiro par de perna do tipo saltatório. Cabeça muito variável quanto à forma. Muitas espécies apresentam cabeça consideravelmente prolongada entre os olhos. Possuem antenas filiformes. O aparelho bucal é mastigador. As fêmeas podem apresentar ovopositor longo com aspectos de laminas. Pernas anteriores e medianas ambulatórias, nas paquinhas o par anterior é fossorial. Na maioria das espécies há dois pares de asas, sendo o anterior do tipo tégmina e o posterior membranoso. A maioria dos orthopteros apresentam tímpanos (órgãos auditivos) localizados de cada lado de cada do primeiro urômetro.",
            "ordem": "Orthoptera",
            "filo": "Arthropoda",
            "classe": "Insecta",
            "reino": "Animalia",
            "inseto": true
        }
  ]
}
```

### Buscar um Inseto

```http
GET /insetos/{:id} HTTP/1.1
```

Retorna o registro do Inseto cujo ID foi recebido.

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID do Inseto a ser pesquisado.|

**Requisição:**

```http
GET /insetos/507f1f77bcf86cd799439011 HTTP/1.1
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
            "_id": "5a25cd076132ff0a62d50adf",
            "info": "São agrupados nessa ordem os gafanhotos, as esperanças, os grilos, as paquinhas e as taquarinhas. Esses insetos possuem o terceiro par de perna do tipo saltatório. Cabeça muito variável quanto à forma. Muitas espécies apresentam cabeça consideravelmente prolongada entre os olhos. Possuem antenas filiformes. O aparelho bucal é mastigador. As fêmeas podem apresentar ovopositor longo com aspectos de laminas. Pernas anteriores e medianas ambulatórias, nas paquinhas o par anterior é fossorial. Na maioria das espécies há dois pares de asas, sendo o anterior do tipo tégmina e o posterior membranoso. A maioria dos orthopteros apresentam tímpanos (órgãos auditivos) localizados de cada lado de cada do primeiro urômetro.",
            "ordem": "Orthoptera",
            "filo": "Arthropoda",
            "classe": "Insecta",
            "reino": "Animalia",
            "inseto": true
        }
    }
}
```

### Editar um Inseto

```http
PUT /insetos/{:id} HTTP/1.1
```

Faz a edição do registro do Inseto.

**Observações:** *Passar somente os atributos que serão atualizados.*

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID do Inseto passado na URL.|
|inseto|Boolean|-|-|-|Não|Caso seja um Inseto.|
|ordem|String|-|-|-|Não|Ordem do Inseto.|
|reino|String|-|-|-|Não|Reino do Inseto.|
|filo|String|-|-|-|Não|Filo do Inseto.|
|classe|String|-|-|-|Não|Classe do Inseto.|
|info|String|-|-|-|Não|Informações do Inseto.|

**Requisição:**

```http
PUT /insetos/507f1f77bcf86cd799439011 HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
   "origem": "América Central, América do Sul"
}
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```

### Editar ou Adicionar atributo a um Inseto

```http
PATCH /insetos/{:id} HTTP/1.1
``` 

Faz a edição de um atributo específico do Inseto.

**Observações:** *Passar somente os atributos que serão atualizados.*

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID do Inseto passado na URL.|
|inseto|Boolean|-|-|-|Não|Caso seja um Inseto.|
|ordem|String|-|-|-|Não|Ordem do Inseto.|
|reino|String|-|-|-|Não|Reino do Inseto.|
|filo|String|-|-|-|Não|Filo do Inseto.|
|classe|String|-|-|-|Não|Classe do Inseto.|
|info|String|-|-|-|Não|Informações do Inseto.|

**Requisição:**

```http
PUT /insetos/507f1f77bcf86cd799439011 HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
  "origem": "América Central, América do Sul"
}
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```

### Deletar um Inseto

```http
DELETE /insetos/{:id} HTTP/1.1
```
Remove o Inseto com o ID passado.


**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID do Inseto a ser removido.|

**Requisição:**

```http
DELETE /insetos/507f1f77bcf86cd799439011 HTTP/1.1
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```


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


## História
Responsável pelas informações das Histórias cadastradas no sistema.

### Adicionar História
Responsável pela adição de uma determinada História.

```http
POST /historias HTTP/1.1
```

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|historia|Boolean|-|-|-|Não|Caso seja uma História.|
|titulo|String|-|-|-|Não|Título da História.|
|localidade|String|-|-|-|Não|Localidade da História.|
|info|String|-|-|-|Não|Informaçãoes da História.|

**Requisição:**
```http
POST /historias HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
            "titulo": "Centro de Visitantes Jeferson da Franca Alencar",
            "info": "Edificação de raro modelo construtivo, construída em taipa com alpendre elevado, piso superior em madeira. Todas as paredes são de taipa de mão com esteios de aroeira/pau d’arco com distância regular entre eles e envaramento de marmeleiro com fixação de cipó, sendo considerada a única casa de taipa de primeiro andar do Estado. Tombada pela Secretaria de Cultura do Estado em 2013. Transformada em Centro de Visitantes em 2017, recebeu o nome do antigo guardião do local.",
            "localidade": "Crato - Ceará",
            "historia": true
}
```

**Resposta:**

```http
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: xxx
Location: /historias/507f1f77bcf86cd799439011
```

### Listar todas as Histórias

```http
GET /historias HTTP/1.1
```

Retorna todas as Histórias.

**Requisição:**

```http
GET /historias HTTP/1.1
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
            "_id": "5a27a6326132ff0a62d50af1",
            "titulo": "Parque Estadual Sítio Fundão – Geossítio Batateiras",
            "info": "Criado pelo Decreto Nº 29.307 de 05/06/2008, na categoria de Unidade de Conservação de Proteção Integral prevista pelo Sistema Estadual de Unidades de Conservação – SNUC, possui como finalidade a prevenção de ecossistemas naturais de grande relevância ecológica e beleza cênica, possibilitando a realização de pesquisas científicas e o desenvolvimento de atividades de educação e interpretação ambiental, de recreação em contato com a natureza e de turismo ecológico. Está localizado no município de Crato – CE e possui uma área de 93,54 ha, apresentando espécies da flora e fauna típicas do bioma Caatinga, edificações históricas tombadas e um pequeno cânion formado pelo rio Batateira, o qual dá nome ao território ao geossítio do Geopark Araripe ( Geossítio Batateiras), área em que está sobreposto, o Pares Sítio Fundão.",
            "localidade": "Crato - Ceará",
            "historia": true
        },
        {
            "_id": "5a2946196132ff0a62d50af3",
            "titulo": "Centro de Visitantes Jeferson da Franca Alencar",
            "info": "Edificação de raro modelo construtivo, construída em taipa com alpendre elevado, piso superior em madeira. Todas as paredes são de taipa de mão com esteios de aroeira/pau d’arco com distância regular entre eles e envaramento de marmeleiro com fixação de cipó, sendo considerada a única casa de taipa de primeiro andar do Estado. Tombada pela Secretaria de Cultura do Estado em 2013. Transformada em Centro de Visitantes em 2017, recebeu o nome do antigo guardião do local.",
            "localidade": "Crato - Ceará",
            "historia": true
        }
  ]
}
```

### Buscar uma História

```http
GET /historias/{:id} HTTP/1.1
```

Retorna o registro da História cujo ID foi recebido.

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID da História a ser pesquisada.|

**Requisição:**

```http
GET /historias/507f1f77bcf86cd799439011 HTTP/1.1
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
            "_id": "5a2946196132ff0a62d50af3",
            "titulo": "Centro de Visitantes Jeferson da Franca Alencar",
            "info": "Edificação de raro modelo construtivo, construída em taipa com alpendre elevado, piso superior em madeira. Todas as paredes são de taipa de mão com esteios de aroeira/pau d’arco com distância regular entre eles e envaramento de marmeleiro com fixação de cipó, sendo considerada a única casa de taipa de primeiro andar do Estado. Tombada pela Secretaria de Cultura do Estado em 2013. Transformada em Centro de Visitantes em 2017, recebeu o nome do antigo guardião do local.",
            "localidade": "Crato - Ceará",
            "historia": true
        }
    }
}
```

### Editar uma História

```http
PUT /historias/{:id} HTTP/1.1
```

Faz a edição do registro da História.

**Observações:** *Passar somente os atributos que serão atualizados.*

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID da História passado na URL.|
|historia|Boolean|-|-|-|Não|Caso seja uma História.|
|titulo|String|-|-|-|Não|Título da História.|
|localidade|String|-|-|-|Não|Localidade da História.|
|info|String|-|-|-|Não|Informaçãoes da História.|

**Requisição:**

```http
PUT /historias/507f1f77bcf86cd799439011 HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
   "titulo": "Centro de Visitantes Jeferson da Franca Alencar"
}
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```

### Editar ou Adicionar atributo a uma História

```http
PATCH /historias/{:id} HTTP/1.1
``` 

Faz a edição de um atributo específico da História.

**Observações:** *Passar somente os atributos que serão atualizados.*

**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID da História passado na URL.|
|historia|Boolean|-|-|-|Não|Caso seja uma História.|
|titulo|String|-|-|-|Não|Título da História.|
|localidade|String|-|-|-|Não|Localidade da História.|
|info|String|-|-|-|Não|Informaçãoes da História.|

**Requisição:**

```http
PUT /historias/507f1f77bcf86cd799439011 HTTP/1.1
Content-Type: application/json
Content-Length: xxx
```
```json
{
  "titulo": "Centro de Visitantes Jeferson da Franca Alencar"
}
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```

### Deletar uma História

```http
DELETE /historias/{:id} HTTP/1.1
```
Remove a História com o ID passado.


**Parâmetros:**

|NOME|TIPO|MÍNIMO|MÁXIMO|FORMATAÇÃO|OBRIGATÓRIO|DESCRIÇÃO|
|----|:--:|:----:|:----:|:--------:|:---------:|---------|
|{:id}|ObjectId|-|-|-|Sim|ID da História a ser removida.|

**Requisição:**

```http
DELETE /historias/507f1f77bcf86cd799439011 HTTP/1.1
```

**Resposta:**

```http
HTTP/1.1 204 No Content
```


