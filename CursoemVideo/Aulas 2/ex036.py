home_valut = int(input('Qual valor da casa: '))
wage_valut = int(input('Qual valor do salário: '))
years_to_pay = int(input('Digite o numero de parcelas: '))

value_of_installments = (home_valut / years_to_pay)

if value_of_installments < wage_valut/100*30:
    print('Emprestimo aprovado!')
    print(f'O valor das parcelas será de {years_to_pay}x de R$: {value_of_installments:.2f}')
elif value_of_installments > wage_valut/100*30:
    print('Execedeu 30% do valor do salario')