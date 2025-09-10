#!/bin/bash

# Проверяем существование файла .env
if [ ! -f ".env" ]; then
  echo "Ошибка: файл .env не найден!"
  exit 1
fi

# Создаем резервную копию
cp .env .env.backup

# Длина токена (по умолчанию 16)
TOKEN_LENGTH=${1:-16}

# Генерируем новый секретный ключ
SECRET_KEY=$(python -c "import secrets; print(secrets.token_urlsafe($TOKEN_LENGTH))")

# Обновляем значение в файле .env
sed -i "s/^SECRET_KEY=.*/SECRET_KEY=$SECRET_KEY/" .env

echo "Старый файл сохранен как .env.backup"
echo "Новый секретный ключ сгенерирован и сохранен в .env:"
echo "SECRET_KEY=$SECRET_KEY"
