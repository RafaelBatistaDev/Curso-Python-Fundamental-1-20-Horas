print("print multiple colors with custom separator")
print("azul", "celeste", "turquesa", "ciano", "verde água", sep="---")
print(   "azul", "celeste", "turquesa", "ciano", "verde água", sep="---")
print('a', 'b', 'c', sep='-', end='*')
print("Tenham", "bons", "estudos")
print('x', 'y', 'z', sep='|', end=' END\n')
print("Fim do exemplo de múltiplos prints com separadores e finais personalizados.")
print('Testando 123', '_')
print('Testando 123', sep='_')
print('Testando 123', end='_')
case_sensitive = True
print('Case Sensitive is', case_sensitive)
def custom_message(msg, repeat=3, sep=' | '):
    print(sep.join([msg] * repeat))

def default_message():
    print("Yan, Maria Clara, Phelipe vcs são o motivo pŕa eu começar a dominar o Python")
    print("A vida se toran melhor quando agente quer.")
    print("Deus é Maior")
default_message()
##### developed by RecifeCrypto #####