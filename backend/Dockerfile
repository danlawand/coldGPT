FROM python:3.9-slim

WORKDIR /app

ENV PIP_ROOT_USER_ACTION=ignore
ENV URL_HOTMART="https://hotmart.com/pt-br/blog/como-funciona-hotmart"
ENV API_LLM_URL="https://api-inference.huggingface.co/models/timpal0l/mdeberta-v3-base-squad2"
ENV API_KEY_HUGGING="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"

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
