from peewee import *
from os import path
connection = path.dirname(path.realpath(__file__))
#create a database called emobilis.db
db =SqliteDatabase(path.join(connection,"emobilis.db"))
#create a table called users in the db
class User(Model):
    name = CharField()
    email = CharField()
    password = CharField()
    #direct the table to be breated inside our db
    class Meta:
        database = db
#finally execute the table creation
User.create_table(fail_silently= True)

class Product(Model):
    productname = CharField()
    productprice = CharField()
    productQtty = CharField()

    class Meta:
        database = db

Product.create_table()