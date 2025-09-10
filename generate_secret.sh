#!/bin/bash

# Создаем файл .env с базовыми настройками
cat << EOF > .env
FLASK_ENV=development
FLASK_DEBUG=1
APP_PORT=5010
EOF

# Генерируем токен
SECRET_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(16))')

# Добавляем SECRET_KEY в файл .env
echo "SECRET_KEY=$SECRET_KEY" >> .env

echo "Файл .env успешно создан:"
cat .env
echo "Секретный ключ: $SECRET_KEY"
