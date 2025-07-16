FROM python:3.11-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache curl bash

# Скачиваем wait-for-it для ожидания базы
RUN curl -o /usr/local/bin/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && chmod +x /usr/local/bin/wait-for-it.sh

RUN pip install --upgrade pip
COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD /usr/local/bin/wait-for-it.sh postgres:5432 -- sh -c "\
    python manage.py migrate && \
    python manage.py shell -c \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'root@example.com', 'root')\" && \
    python manage.py collectstatic --no-input && \
    gunicorn config.wsgi:application --bind 0.0.0.0:8000 --log-level info \
"
