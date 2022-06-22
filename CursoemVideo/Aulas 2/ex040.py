import numpy as np
nota_1 = float(input('Digite sua primeira nota: '))

nota_2 = float(input('Digite sua segunda nota: '))

media = nota_1 + nota_2 / 2

media_float = np.arange(5, 6, 0.1, dtype=float)


if media > 7.0:
    print('Aprovado!')
elif media >= 5 and media <7:
    print('Recuperação')
elif media < 5.0:
    print('Reprovado!')

