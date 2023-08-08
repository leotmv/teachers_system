students = {
    '585454': 'Douglas Martins Renesto',
    '696969': 'Vitor dos Santos Bispo',
    '656463': 'Gustavo Almeida',
    '666666': 'Leonardo Vieira',
    '242424': 'Yuri Delgado',
    '333333': 'Jéssica Nemaniumas',
}
notas = {
    'fis': '',
    'mat': '',
    'qui': '',
}
final = {
    '585454': notas.copy(),
    '696969': notas.copy(),
    '656463': notas.copy(),
    '666666': notas.copy(),
    '242424': notas.copy(),
    '333333': notas.copy()
}
#prog principal

i = 0
while i != 's':
    RA = str(input('Digite o RA: '))
    if RA in students.keys():
        print(students[RA])
        fis = str(input('Nota de física: '))
        mat = str(input('Nota de matemática: '))
        qui = str(input('Nota de química: '))

        final[RA]['fis'] = fis
        final[RA]['mat'] = mat
        final[RA]['qui'] = qui
    else:
        print('RA inválido')
        break
    i = str(input('Deseja sair? Digite s (sim) para sair ou qualquer letra para continuar '))

decisao = str(input('Deseja visualizar somente um ra? Se sim, digite s '))
if decisao.lower() == 's':
    saida = None
    while saida != 'sim':
        RA = str(input('Digite o RA:'))
        print(students[RA])
        print(final[RA])
        saida = str(input('Para sair, digite sim'))
        print('Boletim completo')
        print(final)
else:
    print(final)




