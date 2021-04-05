from pymongo import MongoClient

client = MongoClient('localhost', 27017, username='root', password='root')

db = client['ProductCatalog']

products_collection = db['products']
categories_collection = db['categories']
