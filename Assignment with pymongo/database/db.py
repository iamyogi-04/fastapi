from multiprocessing import connection
from re import M
from pymongo import MongoClient

connection= MongoClient("mongodb://localhost:27017/pymongo")