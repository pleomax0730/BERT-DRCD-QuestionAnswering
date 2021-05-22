FROM python:3.7-slim-buster

WORKDIR /app

COPY ./app.py .

COPY ./requirements.txt .

RUN pip3 install --no-cache-dir -r ./requirements.txt

EXPOSE 8501

# CMD ["streamlit", "run", "app.py"]