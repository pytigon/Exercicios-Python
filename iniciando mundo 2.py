import time
print ('\n APROVAÇÃO DE EMPRESTIMOS TIGON\n')

casa_custo = float(input('Qual o valor do empréstimo que o senhor(a) deseja?\n>>>>> '))
salario = float(input('Qual é a sua renda mesal?\n>>>>> '))
anos = float(input('Quantos anos até o senhor(a) pagar pelo empréstimo?\n>>>>> '))

print('\nAnalizando seus dados...')
time.sleep(1)
meses = anos*12
gasto = casa_custo/meses
margem = 0.3*salario

if gasto>margem:
    print('\nTentativa de empréstimo negada!\nO valor da prestação excede 30% do seu salário.')
    print('Prestação mensal: R${:.2f}'.format(gasto))
else:
    print('\nEmpréstimo realizado com sucesso!\nEsperamos que você realize seus sonhos.')
    print('Prestação mensal: R${:.2f}'.format(gasto))