from flask import Flask,jsonify,request
from main import *
from config import *

app = Flask(__name__)


@app.route("/",methods = ["GET"])
def main():
    return '<h1>Главная страница</h1>'

@app.route("/get_books/",methods = ["GET"])
def get_books():
    books = get_book()
    return jsonify(books)


@app.route("/create_book/",methods = ["POST"])
def create_new_book():
    data = request.get_json()
    new_book = create_book(data)
    return f'Ваша книга {data} была добавлена под id={new_book.id}'


@app.route("/update_book/<int:book_id>/",methods = ["PUT"])
def update(book_id):
    new_book = request.get_json()
    book = update_book(book_id,new_book)
    return f'книга с id = {book} была обновлена'


@app.route("/find_book/<int:book_id>/",methods = ["GET"])
def find_book_(book_id):
    book = find_book(book_id)
    return f'Ваша книга: {book}'

@app.route("/delete_book/<int:book_id>/",methods = ["DELETE"])
def delete(book_id):
    id = delete_book(book_id)
    return f'Книга с id={id} была удалена'




app.run(host='localhost',port=PORT)