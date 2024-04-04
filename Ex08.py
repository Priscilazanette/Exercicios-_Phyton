#valor do dolar com base na cotação do dia 03/04/2024

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.04
print('Com R$ {:.2f} você pode comprar US${:.2}'.format(real, dolar))
