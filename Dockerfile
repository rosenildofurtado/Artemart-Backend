FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN python manage.py makemigrations && python manage.py migrate

RUN ls .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
