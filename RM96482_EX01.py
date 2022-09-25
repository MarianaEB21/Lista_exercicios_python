# Exercício 01
#   Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria:
#   um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube
#   com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma
#   porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.
#
#   Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e
#   que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem
#   de acordo com cada nível de assinatura:

# Definindo variáveis
plano = 0
faturamento_anual: float
porcentagem: float
bonus: float

while (plano < 1 or plano > 4):
    print("PLANOS DISPONÍVEIS")
    print("1 - Basic")
    print("2 - Silver")
    print("3 - Gold")
    print("4 - Platinum")

    try:
        plano = int(input("Digite o número correspondente ao seu plano: "))
    except:
        print('!!! Digite um valor numérico !!!')
    else:
        if plano == 1:
            print(">> Plano Basic")
            porcentagem = 0.3

        elif plano == 2:
            print(">> Plano Silver")
            porcentagem = 0.2

        elif plano == 3:
            print(">> Plano Gold")
            porcentagem = 0.1

        elif plano == 4:
            print(">> Plano Platinum")
            porcentagem = 0.05
        else:
            print("A opção não é válida, digite novamente!")

error_faturamento = True
while error_faturamento:
    try:
        faturamento_anual = float(input("Qual seu faturamento anual? "))
    except:
        print("O faturamento precisa ser numérico! Digite novamente.")
        error_faturamento = True
    else:
        bonus = faturamento_anual * porcentagem
        print(f"Seu bônus será R$ {bonus}")
        error_faturamento = False





