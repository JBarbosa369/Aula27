#leitura da quantidade de alunos (INT)
quantidade_aluno= int(input("digite a quantidade de alunos:"))
#leitura do nome do aluno (string)
Nome = input("digite o nome do aluno:")
#leitura das 4 notas do aluno (FLOAT)
Nota1 = float(input("digite a nota do aluno:"))
Nota2= float(input("digite a nota do aluno:"))
Nota3 = float(input("digite a nota do aluno:"))
Nota4 = float(input("digite a nota do aluno:"))
#leitura da quantidade de faltas do aluno (INT)
faltas = int(input("digite a quantidade de faltas do aluno:"))

Mediadoaluno =(Nota1+Nota2+Nota3+Nota4)/4

    #Solicita os dados do aluno
if faltas <= 31:
    Mediadoaluno = float(input("digite a media do aluno:"))
    #verifica os criterio de aprovação/reprovação
elif faltas >= 31:
    situacao = 'reprovado'
    
elif Mediadoaluno >= 8:
        print("aprovado")
    
elif Mediadoaluno >= 5:
    print("recuperação")
    recuperacao = float(input())
    if Mediadoaluno + recuperacao >=8:
        Mediadoaluno = Mediadoaluno + recuperacao
        print("aprovado")    
else:
    print("reprovado")

print("o aluno está",situacao)