import mongodb_config
from pymongo import MongoClient

def get_databases():

    mongoClient = MongoClient(mongodb_config.connection_string)

    mongoDatabase = mongoClient['project']
    #studentsCollection = mongoDatabase['students']
    #booksCollection = mongoDatabase['books']

    return mongoDatabase


