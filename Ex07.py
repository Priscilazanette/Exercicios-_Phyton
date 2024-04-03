#Jeito Matemático de resolver:

'''co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = co ** + ca ** 2) ** (1/2)
print('A hipotenusa vai medi {:.2f}'.format(hi))'''

#Com importação da classe Math:

import math
co = float(input('Comprimento do catato oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {.:2f}'.format(hi))


