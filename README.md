# HotmartGPT

## Sobre o projeto
Desenvolvido para solucionar o desafio avaliativo para a vaga de Engenheiro de M.L. da [Hotmart](https://hotmart.com/pt-br).

A implementação foi feita pensando na exatidão das respostas, na experiência do usuário, na clareza de código e no tempo de build e execução da aplicação.

A aplicação possui uma interface em que o usuário pode utilizar para fazer perguntas sobre ao HotmartGPT.
O código da interface, implementado com o framework Vue, está localizado no diretório frontend.

No diretório backend está o código do processamento de texto e da construção da LLM. A LLM foi construída com o modelo [mdeberta-v3-base-squad2](https://huggingface.co/timpal0l/mdeberta-v3-base-squad2).


## Requisitos do sistema
1. Instale Docker Engine:

    * Siga o passo-a-passo no link a seguir [Documentação Docker](https://docs.docker.com/engine/install/)

2. Instale Docker-Compose:
    
    * Siga as instruções no link a seguir  [Instalação Docker-Compose](https://docs.docker.com/compose/install/standalone/)

## Como rodar:

### Usando Docker Compose

1. `docker-compose up`
Essa alternativa realiza o pull das imagens do backend e do frontend disponíveis no [Docker Hub](https://hub.docker.com/r/danlawand/) e executa a aplicação de ponta a ponta.
Espere o build das duas imagens para começar a usar a aplicação.


### Usando make
Para realizar o build desta forma, será preciso ter em mãos a chave de API do HuggingFace.
E alterar os arquivos ./backend/.env e ./backend/Dockerfile para adicionar a chave de API.

1. `make front`
Esse comando realiza a construção da imagem do frontend e o executa.

2. `make back`
Esse comando realiza a construção da imagem do backend e o executa.
Espere o build das duas imagens para começar a usar a aplicação.

## Como testar:

### Sugere-se três maneiras para testar a aplicação:

1. Via frontend:

Caso tenha buildado o frontend, você poderá acessar no seu navegador o endpoint `http://localhost:8080` e terá o passo a passo para realizar a pergunta ao HotmartGPT.

2. Via API Client

Nesse caso, não é necessário ter buildado o frontend.
É apenas necessário o uso de um API Client como Postman ou Insomnia.
Para realizar a pergunta ao HotmartGPT, será necessário selecionar o method POST com o endpoint `http://localhost:5000/genai`. O body do request será no formato JSON com o padrão a seguir:

```js
{
    "text": "Sua Pergunta"
}
```

3. Via cURL

Nesse caso também não será preciso buildar o frontend.
Via terminal realize o comando cURL.
Segue um exemplo:

```sh
curl --request POST \
  --url http://localhost:5000/genai \
  --header 'Content-Type: application/json' \
  --data '{
	"text": "Sua Pergunta"
}'
```
Mais testes via cURL estão disponibilizados nos arquivos no diretório `./testes`.
Cada arquivo tem um comando de entrada e o output gerado pelo HotmartGPT.
