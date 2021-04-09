<table align="center"><tr><td align="center" width="9999">

<img src="https://rlv.zcache.com.br/camiseta_t_shirt_do_retrato_de_anton_lavey-r5f62938dcec84f84ac776abf42ff0fac_k21au_307.jpg?rvtype=content" align="center" width="100" alt="Project icon">

# ANTON

*Satanic Bible instructed Artificial Intelligence API*
</td></tr>

</table>    

<div align="center">

> [![Version badge](https://img.shields.io/badge/version-0.0.1-silver.svg)]()


Este serviço disponibiliza uma API GraphQL com modelos de redes neurais recorrentes para gerar texto baseado em exemplos da bíblia satânica de Anton Szandor LaVey.

Uma demo está disponível em: `https://anton.brunolcarli.repl.co/graphql/`
</div>

Exemplo de consulta:


```json
query{
  generatedText{
    text
  }
}
```

Exemplo de resposta:

```json
{
  "data": {
    "generatedText": {
      "text": "inferno católico protestanto satanistas esconhecer satânico sente ondo terrdivedo umo pessoa feverente reques seun condado maprender ser dausadisar diveriades"
    }
  }
}
```

Exemplo com Python

```py
>>> import requests
>>> data = '{generatedText{text}}'
>>> url = 'https://anton.brunolcarli.repl.co/graphql/'
>>> response = requests.post(url, json={'query': data})
>>> response.json()
{'data': {'generatedText': {'text': 'parte veido ou tramisação sexual deriridos seus
 você não pode sandicos iodesso senessosfrente verdo verdade descondecado não setâni
ca dimpreventas emenofulha esanam caminhos encria prazer tantrgia tom temer'}}}
>>>
```

Este projeto é puramente recreacional e não possui fins lucrativos. Todos os direitos de propriedade da Bíblica Satânica pertencem a seu grã criador Anton LaVey.