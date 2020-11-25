from pymongo import MongoClient

class MongoConnect():

    def insert(self, obj):
        try:
            conexao = MongoClient('localhost', 27017)
            banco = conexao.n2linguagemprogramacao
            musica = banco.musica
            id = musica.insert_one(obj).inserted_id

        except Exception as e:
            print(obj)
            print(e)