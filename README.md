# Prompt Engineering Project - coldGPT

## About
Developed to solve the evaluation challenge for a ML Engineer position.

The implementation was made with the accuracy of the answers in mind, the user experience, the clarity of the code and the build and execution time of the application.

The application has an interface that the user can use to ask questions to the coldGPT.
The interface code, implemented with the Vue framework, is located in the frontend directory.

In the backend directory is the code for text processing and building the LLM. The LLM was built using the [mdeberta-v3-base-squad2](https://huggingface.co/timpal0l/mdeberta-v3-base-squad2) model.

## System requirements
1. install Docker Engine:

    * Follow the step-by-step on the following link [Docker Documentation](https://docs.docker.com/engine/install/)

2. Install Docker-Compose:
    
    * Follow the instructions in the following link [Docker-Compose Installation](https://docs.docker.com/compose/install/standalone/)

## How to run:

### Using Docker Compose

1. `docker-compose up`
This alternative pulls the backend and frontend images available on [Docker Hub](https://hub.docker.com/r/danlawand/) and runs the application end-to-end.
Wait for the two images to be built before you start using the application.

### Using make
To build in this way, you'll need the HuggingFace API key.
And change the ./backend/.env and ./backend/Dockerfile files to add the API key.

1. `make front`
This command builds the frontend image and runs it.

2. `make back`
This command builds the backend image and runs it.
Wait for the two images to be built before you start using the application.

## How to test it:

### We suggest three ways to test the application:

1. Via the frontend:

If you have built the frontend, you can access the `http://localhost:8080` endpoint in your browser and you will have the step-by-step instructions for asking coldGPT the question.

2. Via API Client

In this case, you don't need to have built the frontend.
You just need to use an API Client such as Postman or Insomnia.
To make the request to coldGPT, you need to select the POST method with the endpoint `http://localhost:5000/genai`. The body of the request will be in JSON format with the following pattern:

```js
{
    “text": ”Your Question”
}
```

3. Via cURL

In this case you don't need to build the frontend either.
Use the cURL command in the terminal.
Here's an example:

```sh
curl --request POST \
  --url http://localhost:5000/genai \
  --header 'Content-Type: application/json' \
  --data '{
	"text": "Your Question"
}'
```

More tests via cURL are available in the files in the directory `./testes`.
Each file has an input command and the output generated by coldGPT.
