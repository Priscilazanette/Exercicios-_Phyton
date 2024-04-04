largura = float(input('largura da parede:'))
alt  =  float(input('Altura da parede:'))
area = largura * alt
print('sua parede tem dimensao de {}x{} e sua area e de {}m²'.format(largura, alt, area))
tinta = area / 2
print('para pintar esta parede, voce precisará de {}L de tinta.'.format(tinta))