lista_de_convidados =[' Pai', 'Mãe', 'Irmã']
mensagem = ' Venha jantar comigo amanhã '

print(mensagem + lista_de_convidados[0])
print(mensagem + lista_de_convidados[1])
print(mensagem + lista_de_convidados[2])

# exercício 3.5

lista_de_convidados[0] = 'sogra'
print(mensagem + lista_de_convidados[0])
print(mensagem + lista_de_convidados[1])
print(mensagem + lista_de_convidados[2])

print(' Encontramos uma mesa maior para o jantar')
lista_de_convidados.insert(0, 'primo0')
lista_de_convidados.insert(2, 'primo2')
lista_de_convidados.append('primoUlt')

print('Infelizmente só poderemos convidar duas pessoas')

print(lista_de_convidados)
print(len(lista_de_convidados), 'convidados')

lista_de_convidados.pop(0)
lista_de_convidados.pop(1)
lista_de_convidados.pop(2)
lista_de_convidados.pop(0)
print(lista_de_convidados)
lista_de_convidados.__delitem__(0)
lista_de_convidados.__delitem__(0)
print(lista_de_convidados)

