velocidade = int(input('Qual a velocidade? '))
velocidade_max = int(80)
if velocidade < velocidade_max:
    print('Não levou multa!')
elif velocidade <= velocidade_max + 10:
    print('Levou multa leve!')
elif velocidade_max + 11 <= velocidade <= velocidade_max + 20:
    print('Levou multa grave!')
elif velocidade > velocidade_max + 21:
    print('Levou multa gravissima!')
