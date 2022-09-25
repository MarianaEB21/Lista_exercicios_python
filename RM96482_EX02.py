# Exérciocio 02
#   Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives.
#   Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana
#   (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba
#   qual dia foi o escolhido.

dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira","Quinta-feira", "Sexta-feira"]
votos = [0, 0, 0, 0, 0]
k = 0

maior_quantidade_votos = 0
maior_dia_seamana = ''

for voto in votos:
    votos[k] = int(input("Qual a quantidade de votos de  " + dias_semana[k] + ": "))

    if (votos[k] > maior_quantidade_votos):
        maior_quantidade_votos = votos[k]
        maior_dia_seamana = dias_semana[k]

    k = k + 1

print(f"O dia da semana com maior número de votos foi {maior_dia_seamana} com {maior_quantidade_votos} voto(s).")