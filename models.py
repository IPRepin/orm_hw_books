import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


'''создаем классы таблиц'''
class Publisher(Base):
    __tablename__ = "publisher"
    publisher_id = sq.Column(sq.INTEGER, primary_key=True)
    publisher_name = sq.Column(sq.VARCHAR(length=48), unique=True)

    '''Переопределяем метод str для понятного отображения таблицы в консоли'''
    def __str__(self):
        return f'{self.publisher_id}, {self.publisher_name}'

class Book(Base):
    __tablename__ = "book"
    book_id = sq.Column(sq.INTEGER, primary_key=True)
    book_name = sq.Column(sq.VARCHAR(length=100), unique=True)
    id_publisher = sq.Column(sq.INTEGER, sq.ForeignKey('publisher_id'), nullable=False)

    publisher = relationship(Publisher, backref="book")

    '''Переопределяем метод str для понятного отображения таблицы в консоли'''
    def __str__(self):
        return f'{self.id_publisher}: ({self.book_id}, {self.book_name})'

class Shop(Base):
    __tablename__ = "shop"
    shop_id = sq.Column(sq.INTEGER, primary_key=True)
    shop_name = sq.Column(sq.VARCHAR(length=100), unique=True)

    '''Переопределяем метод str для понятного отображения таблицы в консоли'''
    def __str__(self):
        return f'{self.shop_id}, {self.shop_name}'



class Stock(Base):
    __tablename__ = "stock"
    stock_id = sq.Column(sq.INTEGER, primary_key=True)
    id_book = sq.Column(sq.INTEGER, sq.ForeignKey('book_id'), nullable=False)
    id_shop = sq.Column(sq.INTEGER, sq.ForeignKey('shop_id'), nullable=False)
    count = sq.Column(sq.INTEGER, nullable=False)

    shop = relationship(Shop, backref="shop_id")
    book = relationship(Book, backref="book_id")

    def __str__(self):
        return f'{self.stock_id}: ({self.id_book}, {self.id_shop}, {self.count})'

class Sale(Base):
    __tablename__ = "sale"
    sale_id = sq.Column(sq.INTEGER, primary_key=True)
    prise = sq.Column(sq.INTEGER, nullable=False)
    data_sale = sq.Column(sq.DATE, nullable=False)
    id_stock = sq.Column(sq.INTEGER, sq.ForeignKey('stock_id'), nullable=False)
    count = sq.Column(sq.INTEGER, nullable=False)

    stock = relationship(Stock, backref="stock_id")

    def __str__(self):
        return f'{self.stock_id}: ({self.id_book}, {self.id_shop}, {self.count})'

'''Функция создания таблиц'''
def create_tables(engine):
    Base.metadata.create_all(engine)