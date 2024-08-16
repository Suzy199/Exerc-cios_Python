from Surf import patrocinador, atleta, campeonato, campeonato_profissional, campeonato_amador, campeonato_lenda

pat1 = patrocinador('Surf take off', 75000)
pat2 = patrocinador('Big Wave', 50000)
pat3 = patrocinador('Giants of Nazaré', 150000)
pat4 = patrocinador('Medina Foundation', 30000)

atle1 = atleta('Maicon', 19, 2, 'amador')
atle2 = atleta('Brenda', 24, 5, 'amador')
atle3 = atleta('Carlos', 21, 50, 'profissional')
atle4 = atleta('Sherla', 25, 70, 'profissional')
atle5 = atleta('Diego', 20, 130, 'lenda')
atle6 = atleta('Isabela', 22, 150, 'lenda')

patrocinadores = [pat1, pat2, pat3, pat4]
atletas = [atle1, atle2, atle3, atle4]

camp1 = campeonato_amador('amador', 'Campeonato regional','São Paulo', 10000, patrocinadores)
camp2 = campeonato_profissional('profissional', 'Campeonato regional','São Paulo', 30000, patrocinadores)
camp3 = campeonato_lenda('amador', 'Campeonato regional','São Paulo', 50000, patrocinadores)

camp1.todos_atletas(atletas)
camp2.todos_atletas(atletas)
camp3.todos_atletas(atletas)

camp1.vencido_por(atle1)
camp2.vencido_por(atle3)
camp3.vencido_por(atle6)


print("==========================")

print(f'Campeonato :{camp1._nome}: ({camp1._categoria}) em {camp1._local}.')
for a in camp1.lista_de_atletas:
    print("Participante: ", a._nome)
print(f'Vencedor: [{camp1.vencedor}]')


print(f'Campeonato :{camp1._nome}: ({camp2._categoria}) em {camp2._local}.')
for a in camp2.lista_de_atletas:
    print("Participante: ", a._nome)
print(f'Vencedor: [{camp2.vencedor}]')


print(f'Campeonato :{camp3._nome}: ({camp3._categoria}) em {camp3._local}.')
for a in camp2.lista_de_atletas:
    print("Participante: ", a._nome)
print(f'Vencedor: [{camp2.vencedor}]')


print("==========================")