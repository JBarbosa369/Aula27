#Ler entradas do usuario.
cont = 0 #variavel que controla a repetição.
escolha_usuario = int (input())#variavel que guarda quantas vezes o codigo vai rodar.
while cont < escolha_usuario:
    nome = input() #Armazenar o nome do aluno.
    Nota1 = float(input())#4 notas do aluno.
    Nota2 = float(input())
    Nota3 = float(input())
    Nota4 = float(input())

    faltas = int(input())
    #Calculo da media.
    Media = (Nota1+Nota2+Nota3+Nota4)/4

    #Logica da Situação.
    if faltas > 31:
        situacao = "Reprovado por falta"
    elif Media >= 8:
        situacao = "aprovado"
    elif Media >= 5: #Recuperação.
        recuperacao = float(input()) # ler a nota da prova de recuperação.
        if recuperacao >= (10-Media):
            situacao = "Aprovado na recuperação"
        else:
            situacao = "Reprovado na recuperação"
    else:
        situacao = "Reprovado por media"

    #Relatorio.
    print("nome:",nome)
    print("notas:",Nota1,Nota2,Nota3,Nota4)
    print("faltas:",faltas)
    print("media:",Media)
    print("Situacao:",situacao)