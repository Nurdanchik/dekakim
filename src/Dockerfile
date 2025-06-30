FROM python:3.11-alpine

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Отключаем кэширование pyc и включаем буферизацию вывода
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Обновляем pip и копируем requirements
RUN pip install --upgrade pip
COPY requirements.txt .

# Устанавливаем зависимости без кеша
RUN pip install -r requirements.txt --no-cache-dir

# Копируем все исходники
COPY . .

# Выполняем миграции, создаём суперпользователя, собираем статику и запускаем gunicorn
CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'root@example.com', 'root')" \
    && python manage.py collectstatic --no-input \
    && gunicorn config.wsgi:application --bind 0.0.0.0:80 --log-level info