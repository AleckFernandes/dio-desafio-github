name_entry = str(input('Olá Mundo! \n \n Digite seu nome completo:')).strip()

#Seu nome

print('\n Original: ', name_entry,
      '\n Maiusculas: ', name_entry.upper(),
      '\n Minusculas: ', name_entry.lower())

name_entry2 = name_entry.split()
name_entry4 = name_entry2[0]
name_entry3 = ''.join(name_entry2)

print('\n O nome tem: {} letras.'.format(len(name_entry3)),
      '\n O Primeiro nome tem: {} letras.'.format(len(name_entry4)))