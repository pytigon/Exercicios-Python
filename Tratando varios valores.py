result = 0
cont_var = 0
var = 0
while var != 999:
    var = int(input('Digite um numero(\33[31m999\33[m para sair): '))
    if var != 999:
        result += var
        cont_var += 1
print("Você digitou {} números e a soma deles foi {}".format(cont_var, result))