salario_mes = float(input('Digite o valor do salário mensal: '))
horas_trabalhadas = int(input('Qunatas horas trabalhadas: '))
horas_remuneradas = salario_mes / horas_trabalhadas
print('O valor em horas é {:.2f} trabalhando por {} horas'.format(float(horas_remuneradas), horas_trabalhadas))