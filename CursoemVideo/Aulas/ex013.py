# Aumento de % no Salário
valor_salario = float(input('Digite o valor do salário atual:'))
porcentagem_aumento = float(input('Digite a porcentagem desejada:'))
porcentagem_aumento = porcentagem_aumento / 100
porcentagem_aumento = porcentagem_aumento * valor_salario
print('Valor do salário inicial R$:{}'
      '\n Valor do aumento: R${}'
      '\n Novo valor do Salário: R${}'.format(valor_salario, porcentagem_aumento, porcentagem_aumento + valor_salario))
