print('\n   \33[36;4mANALISADOR COMPLETO\33[m\n\n')

soma_idade = 0
media_idade = 0
maior_idade = 0
homem = ''
homem_velho = ''
mulher = ''
mulher_velha = ''
mulher_nova = ''
cont_mulher_nova = 0
maior_idade_homem = 0
maior_idade_mulher = 0
menor_idade_mulher = 0


for dados in range(1, 4+1):
    print('\33[31m----- {}ª PESSOA -----\33[m'.format(dados))
    nome = str(input('Nome: '))
    idade= int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma_idade += idade
    if sexo == 'Mm' and idade > maior_idade_homem:
            maior_idade_homem = idade
            homem_velho = nome
    if sexo == 'Ff' and idade <= 20:
            mulher_nova = nome
            menor_idade_mulher = idade
            cont_mulher_nova += 1


media_idade = soma_idade/4
print('\nA média de idade de todos é ', media_idade)
print('O nome do homem mais velho é {} e ele tem {} anos'.format(homem_velho, maior_idade_homem))
if cont_mulher_nova == 1:
    print('Existe 1 mulher com idade inferior a 20 anos, o nome dela é {} e ela tem {} anos'.format(mulher_nova, menor_idade_mulher))
else:
    print('Existem {} mulheres mais jovens'.format(cont_mulher_nova))
