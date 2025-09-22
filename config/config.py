import mongodb_config
from pymongo import MongoClient


class DatabaseSingleton:
    _instance = None
    _mongoClient = None
    _mongoDatabase = None

    def __new__(cls, connection_string):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._mongoClient = MongoClient(mongodb_config.connection_string)
            cls._mongoDatabase = cls._mongoClient['project']
        return cls._instance

    def get_client(self):
        return self._mongoClient

    def get_database(self):
        return self._mongoDatabase


def get_databases():
    dbInstance = DatabaseSingleton(mongodb_config.connection_string)
    return dbInstance.get_database()
