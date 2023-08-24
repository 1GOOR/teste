

nome = input("escreva aqui -->")

#o Split ele vai cortar a String em partes
#mas quantas pates? A cada 'espaço' ele corta em uma parte
#como no exemplo 'igor josue silva morais' ele divide em 4 partes começando do 0 indo ao 3

#print((nome.split(" "))[1] + '\n')

teste = nome.split()

print(teste)

for i in teste:
    print(teste[1])

