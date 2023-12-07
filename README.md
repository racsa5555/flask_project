================Инструкция по запуску приложения(Windows)======================


# 1.Создание базы данных(postgres)
В терминале пропишите:
psql <user>

create database books

# загрузка зависимостей
Создайте и активируйте venv с помощью команды:
python -m venv venv
cd venv/Scripts
activate.bat

В терминале, находясь внутри папки project_flask пропишите:
pip install -r requirements.txt

# Функционал
http://localhost:8000/get_books/ - возвращает все книги в формате json

http://localhost:8000/create_book/ - создает новую книгу,принимая json c request при этом валидируя данные через Pydantic

http://localhost:8000/update_book/<book_id> - меняет данные книги с id=book_id на получаемый c json

http://localhost:8000/find_book/<book_id> - получает данные книги с id = book_id в формате словаря



