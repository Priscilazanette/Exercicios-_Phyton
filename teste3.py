def escolha_servico():
    while True:

        print('DIG - Digitalizacao \n'
              'ICO - Impressao colorida \n'
              'IBO - Impressao Preto e Branco \n'
              'FOT - Fotocópia \n')

        servico = input('Digite o serviço desejado: ').upper()
        if servico in ['DIG', 'ICO', 'IBO', 'FOT']:
            return servico

        else:
            print('Escolha Inválida!')


def num_pagina():
    while True:

        try:
            numero_paginas = int(input('Digite o Numero de Páginas:'))
            if numero_paginas < 20:
                return numero_paginas
            elif numero_paginas >= 20 and numero_paginas < 200:
                return int(numero_paginas - (numero_paginas * (15 / 100)))
            elif numero_paginas >= 200 and numero_paginas < 2000:
                return int(numero_paginas - (numero_paginas * (20 / 100)))
            elif numero_paginas >= 2000 and numero_paginas < 20000:
                return int(numero_paginas - (numero_paginas * (25 / 100)))
            else:
                print('Numero de páginas excedido!!')
                continue
        except ValueError:
            print('Valor Inválido!!')


def servico_extra():
    while True:
        try:
            print('1 - Encadernação Simples - R$ 15,00')
            print('2 - Encadernação Capa dura - R$ 40,00')
            print('0 - Não desejo mais nada.')
            adicional = int(input('Deseja algum serviço adicional?'))
            if adicional in [0, 1, 2]:
                return adicional
            else:
                print('Opção Inválida!')
                continue

        except ValueError:
            print('Opção Inválida!')


def main():
    try:
        print('Olá! Bem - Vindo a Grafica da Priscila Zanette!!')

        servico = escolha_servico()

        numero_de_paginas = num_pagina()

        adicional = servico_extra()


        # O calculo de custo de serviço

        if servico == 'DIG':
            valor_servico = 1.10 * numero_de_paginas
        elif servico == 'ICO':
            valor_servico = 1.00 * numero_de_paginas
        elif servico == 'IBO':
            valor_servico = 0.40 * numero_de_paginas
        elif servico == 'FOT':
            valor_servico = 0.20 * numero_de_paginas

        #Calculo do Serviço Extra

        if adicional == 1:
            valor_servico += 15
        elif adicional == 2:
            valor_servico += 40


        print(f'Serviço Escolhido: {servico}')
        print(f'Numero de Páginas: {numero_de_paginas}')
        print(f'Adicional: {adicional}')
        print(f'Valor Total à Pagar R$ : {valor_servico:.2f} ')


    except ValueError:
            print('Erro')

main()
