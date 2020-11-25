from musica import Musica

colecao = Musica()

nome = str(input("Informe o nome da música: "))
autor = str(input("Informe o autor: "))
genero = str(input("Informe o gênero da música: "))

colecao.insert(nome, autor, genero)