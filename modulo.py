def leiaInt(n):
  while True:
    try:
      a = int(input(n))
    except :
      print('Erro! Digite um número valido')
    else:
      return a
def validarAno(ano):
  from datetime import date
  
  ano_atual = date.today().year
  while True:
    try:
      a = int(input(ano))
    except :
      print('Erro! digite apenas numeros')
    else:
      if len(str(a)) == 4 and a <= ano_atual:
        return a
      else:
        print('Ano Invalido')
def disposicao(livro):
  v = True
  while True:
    a = str(input(livro)).strip().lower()[0]
    if a in 'sn':
      break
    print('Erro! Digite apenas sim ou não')
  if a == 's':
    return v
  else:
    v = False
    return v
def validarID(number, bi):
  while True:
    try:
      a = int(input(number))
      if a != 0 and a not in bi:
        return a
    except:
      print('Erro! digite apenas numeros')
    else:
      print('Erro! ID Incorreto ou ja existente')