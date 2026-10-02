import json
from modulo import leiaInt
def carregar(arq):
  try:
    with open(arq, 'r') as a:
      return json.load(a)
  except:
    return []
def adicionar(arq, biblio):
  try:
    with open(arq, 'w') as a:
      json.dump(biblio, a, indent=2)
  except:
    print('Erro ao adicionar livro!')
def buscar(biblioteca):
  print('=' * 45)
  print('livros'.center(45))
  print('=' * 45)
  for i, v in enumerate(biblioteca):
    print(f'ID {v["ID"]}. Titulo: {v["titulo"]}')
  while True:
    print("-"*45)
    opc = input('Procurar por [1]ID ou [2]titulo (999 para parar): ')
    if opc == '999':
      break
    if opc == '1':
      pro = leiaInt('ID do livro: ')
      print("="*45)
      for i in biblioteca:
        if i['ID'] == pro:
          print(f"ID {i['ID']}. {i['titulo']}:\n Autor: {i['autor']}\n Ano: {i['ano']}, Disponivel: {i['disponivel']}")

    elif opc == '2':
      pro = input('titulo do livro: ')
      print("="*45)
      for i in biblioteca:
        if i['titulo'].lower() == pro.lower():
          print(f"ID {i['ID']}. {i['titulo']}:\n Autor: {i['autor']}\n Ano: {i['ano']}, Disponivel: {i['disponivel']}")
  
def excluir(arq, bi):
  if bi:
   for i, v in enumerate(bi, start=1):
     print(f'N° {i}. {v["titulo"]}')
   try:
     print()
     indice = leiaInt('N° do Livro: ')-1
     if 0 <= indice <= len(bi):
       excluido = bi.pop(indice)
       adicionar(arq, bi)
       print(f'Livro ID {excluido["ID"]} com Sucesso')
     else:
       print('Erro! N° de livro nao achado!')
   except:
     print('Erro! numero invalido')
  else:
    print('Nenhum livro para excluir')