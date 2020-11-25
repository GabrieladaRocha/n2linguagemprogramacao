from controller import ControllerDb
db = ControllerDb()

autor = str(input("Informe o autor: "))
nome = str(input("Informe o nome da música: "))
genero = str(input("Informe o gênero da música: "))
db.insert(nome, autor, genero)
db.find()
