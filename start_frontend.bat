@echo off
title Frontend Server (npm run dev)

echo --- 1. Changing Directory to vue-project ---
cd vue-project

echo.
echo --- 2. Installing Dependencies (Optional: uncomment if needed) ---
call npm install

call npm run dev

:: Эта часть будет достигнута только после остановки сервера (Ctrl+C)
echo Frontend server stopped.
pause