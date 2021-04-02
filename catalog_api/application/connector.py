from pymongo import MongoClient

client = MongoClient('db_mongo', 27017, username='root', password='root')

db = client['ProductCatalog']

products_collection = db['products']
categories_collection = db['categories']
