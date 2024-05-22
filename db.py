from peewee import * 
from datetime import datetime 
 
 
db = SqliteDatabase("bd.db") 
 
class BaseModel(Model): 
    class Meta: 
        database = db 
 
 
class User(BaseModel): 
    id = AutoField(primary_key=True) 
    name = TextField() 
    adres = TextField(null=True) 
    phone = IntegerField(default=0) 
    email = TextField() 
    admin = IntegerField(default=0) 
 
class Provider(BaseModel): 
    id = AutoField(primary_key=True) 
    name = TextField() 
    adres = TextField(default=None) 
    phone = IntegerField(default=0) 
    email = TextField() 
 
class Payments(BaseModel): 
    id = AutoField(primary_key=True) 
    user = ForeignKeyField(User,backref='users' ) 
    status = IntegerField(default=0) 
 
class Card(BaseModel): 
    id = AutoField(primary_key=True) 
    name = TextField() 
    description = TextField() 
    price = IntegerField() 
    date_live = IntegerField(null=True) # срок жизни товара 
    image = TextField(null=True) #массив [] 
 
 
#заказ ме 
class Order_provider(BaseModel): 
    id = AutoField(primary_key=True) 
    date = DateTimeField(default=datetime.now()) 
    count = IntegerField() 
    price = IntegerField() 
    id_product = ForeignKeyField(Card,backref='Card') 
    provider = ForeignKeyField(Provider, backref='provider')  
 
 
class Order(BaseModel): 
    id = AutoField(primary_key=True) 
    price = IntegerField() 
    count = IntegerField() 
    author = ForeignKeyField(User, backref='user') 
    id_payments = ForeignKeyField(Payments, backref='payments') 
    id_product = ForeignKeyField(Card,backref='Card') 
    date_start = DateTimeField(default=datetime.now()) 
    date_end = DateTimeField(null=True) 
 
 
db.create_tables([User, 
                  Order_provider, 
                  Order, 
                  Card, 
                  Provider, 
                  Payments])