valor = float(input('5'))
escolha = float(input('Digite 1 para calcular o dobro, ou outra coisa para calcular a metade:'))
if escolha == 1:
            dobro = 2 * valor
            print(f'O dobro de {valor} é {dobro}')
else:
            metade = valor / 2
            print(f'A metade de {valor} é {metade}')
print('Fim do programa')
