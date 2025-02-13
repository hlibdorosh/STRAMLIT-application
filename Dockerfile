# Используем официальный Python-образ в качестве базового
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем содержимое текущей директории в контейнер в папку /app
COPY . /app

# Устанавливаем необходимые пакеты, указанные в requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Делаем порт 8501 доступным вне контейнера
EXPOSE 8501

# Запускаем приложение Streamlit при старте контейнера
CMD ["streamlit", "run", "app.py"]
