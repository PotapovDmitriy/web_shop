from pymongo import MongoClient

client = MongoClient('db_mongo', 27017, username='root', password='root')

db = client['ProductCatalog']

cart_collection = db['carts']
