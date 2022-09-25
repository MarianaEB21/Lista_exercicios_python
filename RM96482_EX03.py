#3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.
#Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte padrão:
#VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
#POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.

chamada_impar = []
chamada_par = []
qtde_alunos = 51
media_impar = 0
media_par = 0

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES\n")
for aluno_impar in range (1,qtde_alunos,2):
    nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO {aluno_impar}: "))
    chamada_impar.append(nota)
media_impar = (sum(chamada_impar)/len(chamada_impar))
print("\n")

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES\n")
for aluno_par in range (2,qtde_alunos,2):
    nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO {aluno_par}: "))
    chamada_par.append(nota)
media_par = (sum(chamada_par)/len(chamada_par))

if media_impar > media_par:
    print("A maior média foi dos alunos ímpares, no valor de {:.2f}".format(media_impar))
else:
    if media_impar == media_par:
        print("A média dos alunos pares e ímpares é igual a {:.2f}".format(media_impar))
    else:
        print("A maior média foi dos alunos pares, no valor de {:.2f}".format(media_par))