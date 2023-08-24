
#A string é vista com Um vetor, com o conteudo podendo ser dividido e lida cada caracter individualmente.
nome = "pedro"
#O length serve para ler o comprimento de ojetos como Strings.
print(nome[1:4])
print(len(nome))

n = range(50)
print(n)

#comando mutavel ele nao modifica permanete o objeto(ex [temos um string com o valor de 'IGOR JOSUE' podemos
#dividir ela utilizando um extecao da String .sprint(' ')
# ])

for i in range(1, 11):
    for x in range(1, 11):
        print(f'{x}x{x} = {i}')