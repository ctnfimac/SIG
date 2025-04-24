FROM python:3.10

WORKDIR /code

COPY requeriments.txt .
RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]