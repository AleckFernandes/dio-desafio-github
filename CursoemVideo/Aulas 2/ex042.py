
line_1 = int(input('Digite um numero: '))
line_2 = int(input('Digite um numero: '))
line_3 = int(input('Digite um numero: '))

if line_1 < line_2 + line_3:
    if line_2 < line_1 + line_3:
        if line_3 < line_2 + line_1:
            print('é possivel criar um triangulo')
        else:
            print('não é psossivel')
    else:
        print('não é psossivel')
else:
    print('não é psossivel')
