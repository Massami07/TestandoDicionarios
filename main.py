aluno = {}
chamada = []
ativador = int

while ativador != 0:
    aluno['nome'] = str(input('Qual e o nome do aluno?'))
    aluno['sexo'] = str(input('Qual e o sexo do aluno?'))
    aluno['idade'] = str(input('Qual e a idade do aluno?'))
    chamada.append(aluno.copy())
    aluno.clear()
    ativador = int(input('Digite 0 para parar e qualquer outro numero para continuar'))

print(chamada)
