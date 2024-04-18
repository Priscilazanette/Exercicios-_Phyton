lista_livro = []
def cadastrar_livro(id):
    nome = str(input('Nome:'))
    autor = str(input('Autor:'))
    editora = str(input('Editora:'))
    livro = {'id': id,
             'nome': nome,
             'autor': autor,
             'editora': editora}
    lista_livro.append(livro)
    print('Livro Cadastrado com Sucesso!!')

def consultar_livro():
    if not lista_livro:
        print('-' * 50)
        print('Ainda não há livros cadastrados!')
        return

    while True:
        opcao = int(input('Qual opção deseja?:\n1. Consultar todos\n2. Consultar por ID\n3. Consultar por Autor\n4. Retornar ao menu'))
        print('-' * 50)

        if opcao == 1:
            print('-' * 5 + 'Menu: Todos os Livros:' + '-' * 5)
            for livro in lista_livro:
                print(f'ID: {livro["id"]}')
                print(f'Nome: {livro["nome"]}')
                print(f'Autor: {livro["autor"]}')
                print(f'Editora: {livro["editora"]}')


            print('-' * 50)
        elif opcao == 2:
            print('-' * 5 + 'Menu: Consultar por ID:' + '-' * 5)
            id = int(input('Digite o ID:'))
            for livro in lista_livro:
                if livro['id'] == id:
                    print(f'ID: {livro["id"]}')
                    print(f'Nome: {livro["nome"]}')
                    print(f'Autor: {livro["autor"]}')
                    print(f'Editora: {livro["editora"]}')
                    break
                else:
                    print('Não foi possivel localizar!')
        elif opcao == 3:
            print('-' * 5 + 'Menu: Consultar por Autor:' + '-' * 5)
            autor = str(input('Digite o Nome do Autor:'))
            print(f'Resultado da Busca pelo Autor : {autor}')
            for livro in lista_livro:
                if livro['autor'] == autor:
                    print(f'ID: {livro["id"]}')
                    print(f'Nome: {livro["nome"]}')
                    print(f'Autor: {livro["autor"]}')
                    print(f'Editora: {livro["editora"]}')
                    break
                else:
                    print('Nenhum resultado encontrado!')

        elif opcao == 4:
            return
        else:
            print('Opção inválida. Por favor, Digite uma opção válida.')

def remover_livro():
    id_livro = int(input('Digite o ID do Livro que deseja excluir.'))
    for livro in lista_livro:
        if livro['id'] == id_livro:
            lista_livro.remove(livro)
            print('Livro removido com sucesso!!')
            break
        else:
            print('Livro não encontrado!')


def main():
    print('Bem-Vindo a Biblioteca da Priscila (4649834)!')

    global lista_livro

    id_global = 0
    while True:
        print('-' * 25 + 'MENU PRINCIPAL' + '-' * 25)
        print('1. Cadastrar Livro\n2. Consultar Livro\n3. Remover Livro\n4. Encerrar Programa')
        opcao = int(input())
        if opcao == 1:
            id_global = id_global + 1
            cadastrar_livro(id_global)
        elif opcao == 2:
            consultar_livro()
        elif opcao == 3:
            remover_livro()
        elif opcao == 4:
            print('Encerrando...')
            break
        else:
            print('Opção inválida! Por favor, Digite uma opção válida.')

main()







