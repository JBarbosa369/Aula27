#leitura da quantidade de alunos (INT)
Quantidade_alunos = int(input("digite a quantidade de alunos:"))
#leitura do nome do aluno (string)
Nome = input("digite o nome do aluno:")
#leitura das 4 notas do aluno (FLOAT)
Notas = float(input("digite a nota [i+1] do aluno:"))
#leitura da quantidade de faltas do aluno (INT)
Quantidade_faltas = int(input("digite a quantidade de faltas do aluno:"))

Mediadoaluno =(Notas+Notas+Notas+Notas)/4

while True:
    #Solicita os dados do aluno
    Mediadoaluno = float(input("digite a media do aluno:"))
    Quantidade_faltas = int(input("digite o numero de faltas do aluno:"))

    #verifica os criterio de aprovação/reprovação
    if Quantidade_faltas > 31:
        print("Reprovado por faltas")
    elif Mediadoaluno >= 8:
        print("aprovado")
    elif Mediadoaluno >= 5:
        print("recuperação")
    else:
        print("reprovado por nota")