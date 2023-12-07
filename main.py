from sqlalchemy import create_engine,Column,Integer,String,Date,update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from config import *

DATABASE_URL = "postgresql://"+user+":"+password+"@localhost/"+ name_database
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer,primary_key = True, autoincrement = True)
    title = Column(String,nullable = False,unique = True)
    author = Column(String)
    genre = Column(String,nullable = False)
    created_at = Column(Date())

Base.metadata.create_all(bind = engine)

ItemPydantic = sqlalchemy_to_pydantic(Book,exclude = ["id"])

def create_book(item):
    with SessionLocal() as db:
        db_item = ItemPydantic(**item)
        book = Book(**db_item.dict())
        db.add(book)
        db.commit()
        db.refresh(book)
    return book

def get_book():
    mas_books = []
    with SessionLocal() as db:
        books = db.query(Book).all()
        for book in books:
            mas_books.append({'id':book.id,
                              'title':book.title,
                              'author':book.author,
                              'genre':book.genre,
                              'date_create':book.created_at})
        return mas_books
        
def find_book(book_id):
    with SessionLocal() as db:
        book = db.query(Book).get(book_id)
        return {'id':book.id,
                'title':book.title,
                'author':book.author,
                'genre':book.genre,
                'date_create':book.created_at}
    

def update_book(book_id,book):
    with SessionLocal() as db:
            db_item = ItemPydantic(**book)
            book_up = Book(**db_item.dict())
            for field,value in vars(book_up).items():
                setattr(book_up,field,value)
            db.commit()
            b = db.query(Book).get(book_id)
            return b.id


def delete_book(book_id):
    with SessionLocal() as db:
        del_book = db.query(Book).filter_by(id=book_id).first()
        db.delete(del_book)
        db.commit()
        return del_book.id


# print(create_book({'title':'book1','author':'author1','genre':'genre1','created_at':'2021-02-02'}))
# print(get_book())

        
