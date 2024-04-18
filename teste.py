#Menu de boas -vindas do cliente
nome = input('Qual é o seu nome?').capitalize()
print('Olá, {}. Seja Bem-Vindo(a) a loja de gelados Priscila Zanette!'.format(nome))
print('-' * 25 + 'Cardápio' + '-' * 25)
print('-'*6 + '|' +'   Tamanho  ' + '|' + '  Cupuaçu (CP)  ' + '|' + '  Açaí (AC)  ' + '|'+ '-'*6)
print('-'*6 + '|' +'       P    ' + '|' + '    R$  9,00    ' + '|' + '  R$ 11,00   ' + '|'+ '-'*6)
print('-'*6 + '|' +'       M    ' + '|' + '    R$  14,00   ' + '|' + '  R$ 16,00   ' + '|'+ '-'*6)
print('-'*6 + '|' +'       G    ' + '|' + '    R$  18,00   ' + '|' + '  R$ 20,00   ' + '|'+ '-'*6)
print('-'*59)

total = 0

while True:
       # Exigência de Código 2 e 3: Input do sabor e tamanho com validação
       while True:
              sabor = input('Digite o sabor desejado (CP para Cupuaçu ou AC para Açaí): ').upper()
              if sabor not in ['CP', 'AC']:
                     print('Sabor inválido. Tente novamente.')
                     continue
              else:
                     break
       while True:
              tamanho = input('Digite o tamanho desejado (P para Pequeno, M para Médio ou G para Grande): ').upper()
              if tamanho not in ['P', 'M', 'G']:
                     print('Tamanho inválido. Tente novamente.')
                     continue
              else:
                     break

       if sabor == 'CP':
              if tamanho == 'P':
                     total += 9
                     print('Tamanho P de Cupuaçu custa R$ 9,00')
              elif tamanho =='M':
                     total +=  14
                     print('Tamanho M de Cupuaçu (CP) custa R$ 14,00')
              elif tamanho == 'G':
                     total +=  18
                     print('Tamanho G de Cupuaçu (CP) custa R$ 18,00')

       elif sabor == 'AC':
              if tamanho =='P':
                     total += 11
                     print('Tamanho P de Açaí (AC) custa R$ 11,00')
              elif tamanho == 'M':
                     total +=  16
                     print('Tamanho M de Açaí (AC) custa R$ 16,00')
              elif tamanho == 'G':
                     total +=  20
                     print('Tamanho G de Açaí (AC) custa R$ 20,00')

       pergunta = input('Deseja pedir mais alguma coisa? (S/N):').upper()

       if pergunta != 'S':
              break

print('O valor total dos seus pedidos é R$ {:.2f}'.format(total))

