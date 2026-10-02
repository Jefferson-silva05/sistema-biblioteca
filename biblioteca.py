from modulobiblioteca import *
from arquivo_biblioteca import *
from time import sleep
arq = 'python/projetos/biblioteca/biblioteca.json'
biblioteca = carregar(arq)

print('=' * 45)
print('Sistema Biblioteca'.center(45))
print('=' * 45)
while True:
  print('''[ 1 ] Adicionar Livro
[ 2 ] Listar Livros
[ 3 ] Buscar Livro(ID ou titulo)
[ 4 ] Atualizar Disponibilidade
[ 5 ] Remover Livro
[ 6 ] Sair''')
  opc = leiaInt('Sua Opção: ')
  match opc:
    case 1:
      ID = validarID('ID (3 digitos numericos): ', biblioteca)
      titulo = str(input('Titulo: '))
      autor = str(input('Autor: '))
      ano = validarAno('ano de publicação: ')
      disponivel = disposicao('Disponivel (sim/não): ')
      dic = {'ID': ID, 'titulo': titulo, 'autor': autor, 'ano': ano, 'disponivel': disponivel}
      biblioteca.append(dic)
      adicionar(arq, biblioteca)
      print('Adicionado com Sucesso')
    case 2:
      if biblioteca:
        print('=' * 45)
        print('Listando todos os livros'.center(45))
        print('=' * 45)
        for i, v in enumerate(biblioteca, start=1):
          print(f'ID {v["ID"]}. {v["titulo"]}:\n Autor: {v["autor"]},\n Ano Publicado: {v["ano"]}, Disponivel: {v["disponivel"]}')
          print("- -"*15)
          sleep(0.7)
      else:
        print("Nenhum Livro Adicionado!")
    case 3:
      if biblioteca:
        buscar(biblioteca)
    case 4:
      print('=' * 45)
      print('Disponibilidade de Livros'.center(45))
      print('=' * 45)
      for i, v in enumerate(biblioteca):
        print(f'ID {v["ID"]} - {v["titulo"]}\n Disponivel: {v["disponivel"]}')
      print()
      pro = leiaInt('ID do Livro: ')
      for i in biblioteca:
        if i['ID'] == pro:
          d = disposicao('Disponivel: (sim/nao): ')
          i['disponivel'] = d
          adicionar(arq, biblioteca)
          print('Atualizado com Sucesso!')
          break
      else:
        print('Erro! ID incorreto')
    case 5:
      print('=' * 45)
      print('Excluir livro'.center(45))
      print('=' * 45)
      excluir(arq, biblioteca)
    case 6:
      print('Saindo...')
      sleep(1.7)
      break
    case _:
      print('Erro! Digite uma das opcoes')
  sleep(0.8)
  print("="*45)
print('Volte Sempre')