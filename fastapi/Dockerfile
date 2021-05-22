FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# copy "app" to "root_dir/app"
COPY ./app /app

COPY ./requirements.txt /app

# cd "root_dir/app"
WORKDIR /app

EXPOSE 8000

RUN pip3 install --no-cache-dir -r ./requirements.txt

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]