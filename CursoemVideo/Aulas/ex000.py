

n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('='*30)
print('Resultados: \n'
      '\n Soma: {:>20} '
      '\n Produto: {:>17} '
      '\n Divisão: {:>17.2f} '
      '\n Divisão inteira: {:>9} '
      '\n Potência: {:>16}'.format(s, m, d, di, e))
print('='*30)
