from connection import MongoConnect

class Music():

    def save(self, nome, autor, genero):
        conexao = MongoConnect()
        model = {
            "nome": nome,
            "autor": autor,
            "genero": genero
        }
        conexao.insert(model)