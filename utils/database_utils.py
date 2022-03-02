import certifi
from mongoengine import connect


class DatabaseUtils:
    @staticmethod
    def init_local_db(database_name="py_project1"):
        alias = connect(database_name)



    @staticmethod
    def init_cluster_db(MONGO_URI, database_name="py_project1"):
        ca = certifi.where()
        alias = connect(database_name, host=MONGO_URI, tlsCAFile=ca)

