import math
cateto_b = int(input('Digite o valor do cateto B: '))
cateto_c = int(input('Digite o valor do cateto C: '))
cateto_b = cateto_b**2
cateto_c = cateto_c**2
hipo = cateto_b + cateto_c

print('A hipotenusa é {:.0f}'.format(math.sqrt(hipo)))