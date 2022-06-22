from datetime import date
idade = int(input('Digite sua ano de nascimento: '))
idade = date.today().year - idade
print(idade)
if idade <= 9:
    print('Mirim')
elif idade >= 14 and idade < 19:
    print('Infantil')
elif idade >= 19 and idade < 20:
    print('Junior')
elif idade == 20:
    print('Senior')
elif idade > 20:
    print('Master')
