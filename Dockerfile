# FROM python:3.8-slim-buster
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# copy "app" to "container/app"
COPY ./app /app

COPY ./requirements.txt /app

WORKDIR /app

EXPOSE 80

RUN pip3 install --no-cache-dir -r ./requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]