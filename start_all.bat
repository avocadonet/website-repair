@echo off
title Full Project Launch

:: 1. Запуск бекенда и заполнение БД (Команда 'call' выполняет скрипт и ждет его завершения)
echo [STEP 1/2] Running Backend Setup (start_backend.bat)...
call start_backend.bat

:: 2. Запуск фронтенда в новом окне ('start' запускает в новом окне, '/k' держит его открытым)
echo [STEP 2/2] Running Frontend Server in a NEW SEPARATE WINDOW...
start "Frontend Development Server" cmd /k call start_frontend.bat

timeout /t 5 >nul
exit