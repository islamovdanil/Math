FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN chmod +x generate_secret.sh && \
    chmod +x .env && \
    chmod 644 docker-compose.yml && \
    chmod 644 Dockerfile && \
    chmod -R 644 /app/templates && \
    chmod -R 644 /app/static

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Используем gunicorn для продакшена
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
