FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы requirements.txt и устанавливаем зависимости
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . .

# Устанавливаем переменную окружения для Flask
ENV FLASK_APP=run.py

# Открываем порт 5000 для Flask-приложения
EXPOSE 5000

# Команда для запуска Flask-приложения
CMD ["flask", "run", "--host=0.0.0.0"]