import json
from modulo import leiaInt
def carregar(arq): #carrega arquivo json ou retrona uma lista vazia caso json não exista
  try:
    with open(arq, 'r') as a:
      return json.load(a)
  except:
    return []

def adicionar(arq, biblio): #adiciona novos livros e tambem atualiza status de livros
  try:
    with open(arq, 'w') as a:
      json.dump(biblio, a, indent=2)
  except:
    print('Erro ao adicionar livro!')

def buscar(biblioteca):
  print('=' * 45)
  print('livros'.center(45))
  print('=' * 45)
  print("ADICIONADOS RECENTEMENTE")
  print("-"*45)
  for i, v in enumerate(biblioteca[-3:]):
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
    print("ADICIONADOS RECENTEMENTE")
    print("-"*45)

    for i, v in enumerate(bi[-3:]):
      print(f'ID {v["ID"]}. {v["titulo"]}')

    ID = leiaInt('ID do Livro: ')

    for indice, livro in enumerate(bi):
      if livro['ID'] == ID:
        excluido = bi.pop(indice)
        adicionar(arq, bi)
        print(f'Livro ID {excluido["ID"]} removido com Sucesso')
        break
    else:
      print('Erro! ID de livro não encontrado!')

  else:
    print('Nenhum livro para excluir')

def carregar_livros_testes(arq): #def para acrescentar livros predefinidos no json, sem a necessidade de add manualmente. para fins de teste
    biblioteca = carregar(arq)

    livros_teste = [
        {
            "ID": 1,
            "titulo": "O Pequeno Príncipe",
            "autor": "Antoine de Saint-Exupéry",
            "ano": 1943,
            "disponivel": True
        },
        {
            "ID": 2,
            "titulo": "1984",
            "autor": "George Orwell",
            "ano": 1949,
            "disponivel": False
        },
        {
            "ID": 3,
            "titulo": "Orgulho e Preconceito",
            "autor": "Jane Austen",
            "ano": 1813,
            "disponivel": True
        },
        {
            "ID": 4,
            "titulo": "O Hobbit",
            "autor": "J. R. R. Tolkien",
            "ano": 1937,
            "disponivel": True
        },
        {
            "ID": 5,
            "titulo": "Jane Eyre",
            "autor": "Charlotte Brontë",
            "ano": 1847,
            "disponivel": False
        },
        {
            "ID": 6,
            "titulo": "Emma",
            "autor": "Jane Austen",
            "ano": 1815,
            "disponivel": True
        },
        {
            "ID": 7,
            "titulo": "O Morro dos Ventos Uivantes",
            "autor": "Emily Brontë",
            "ano": 1847,
            "disponivel": False
        },
        {
            "ID": 8,
            "titulo": "As Aventuras de Alice no País das Maravilhas",
            "autor": "Lewis Carroll",
            "ano": 1865,
            "disponivel": True
        },
        {
            "ID": 9,
            "titulo": "Crime e Castigo",
            "autor": "Fiódor Dostoiévski",
            "ano": 1866,
            "disponivel": True
        },
        {
            "ID": 10,
            "titulo": "O Profeta",
            "autor": "Khalil Gibran",
            "ano": 1923,
            "disponivel": False
        }
    ]

    biblioteca.extend(livros_teste)
    adicionar(arq, biblioteca)

    return biblioteca