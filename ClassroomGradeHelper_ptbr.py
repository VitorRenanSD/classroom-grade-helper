import numpy as np
import webbrowser
from time import sleep

qtde_mat = int(input('Quantidade de materias: '))
media_escola = float(input('Média escolar: '))
print('\033[33m------Informações básicas salvas!------\033[0m')
sleep(0.4)

materias = []

for i in range(qtde_mat):
    materia = str(input(f'Nome da {i+1}º matéria: '))
    notas = str(input(f'Notas das provas (separadas por espaço): ')).split()
    print('\033[33m---------Matéria/Notas salvas!---------\033[0m')
    sleep(0.4)
    notas = [float(nota) for nota in notas]
    materias.append([materia] + notas)

print('\033[33m-------------Processando...------------\033[0m')
sleep(0.7)

for materia in materias:
    nome = materia[0]
    notas = np.array(materia[1:])
    media = np.mean(notas)
    status = '\033[32mAprovado\033[0m' if media >= media_escola else '\033[31mRecuperacao\033[0m'
    print(f'\033[1;33mMatéria:\033[0m {nome:25} \033[1;33mMédia:\033[0m {media:.2f} \033[1;33mStatus:\033[0m {status}')

sleep(2.0)
print('\033[35mFeito por: VitorRenanSD\033[0m')
webbrowser.open('https://www.codewars.com/users/VIC_BR')
