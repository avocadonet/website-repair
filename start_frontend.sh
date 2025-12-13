#!/bin/bash

cd vue-project || exit

echo "--- 2. Installing Dependencies (Optional: uncomment if needed) ---"
# Если зависимости уже установлены, можно закомментировать/удалить следующую строку:
npm install

# Эта команда блокирует скрипт, пока сервер не будет остановлен (Ctrl+C).
npm run dev

echo "Frontend server stopped."