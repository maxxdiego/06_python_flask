aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno['Nome']}: '))
aluno['Situação'] = 'Reprovado' if aluno['Média'] < 6 else 'Aprovado'
for k, v in aluno.items():    
    print(f'- {k} é igual a {v}.')