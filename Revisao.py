#Ler entradas do usuario.
#o codigo lendo varios alunos e a mesma coisa
#a unica diferença é que ele está dentro de uma repetição 
 #variavel que controla a repetição.
Menu = int (input()) # variavel que guarda qual escolha do usuario.
Aluno =[]#lista que guardará todos os dados dos alunos cadastrado.
if Menu == 1:
    situacao = ""

    escolha_usuario = int (input("digite quantos alunos e deseja cadastrar:"))
    cont = 0 #variavel que guarda quantas vezes o codigo vai rodar.

   
    while cont < escolha_usuario:
        nome = input("digite o nome do aluno:") #Armazenar o nome do aluno.
        Nota1 = float(input("digite a nota do 1° bimestre:"))#4 notas do aluno.
        Nota2 = float(input("digite a nota do 2° bimestre:"))
        Nota3 = float(input("digite a nota do 3° bimestre:"))
        Nota4 = float(input("digite a nota do 4° bimestre:"))

        faltas = int(input("digite as faltas dos aluno:"))
        #Calculo da media.
        Media = (Nota1+Nota2+Nota3+Nota4)/4

        #Logica da Situação.
        if faltas > 31:
            situacao = "Reprovado por falta"
        elif Media >= 8:
            situacao = "aprovado"
        elif Media >= 5: #Recuperação.
            recuperacao = float (input("digite a nota da recuperação:")) # ler a nota da prova de recuperação.
            if recuperacao >= (10-Media):
                situacao = "Aprovado na recuperação"
            else:
                situacao = "Reprovado na recuperação"
        else:
            situacao = "Reprovado por media"

#enviar os dados do aluno para a lista alunos
    Aluno.append([nome,faltas,Media,situacao])
    cont = cont +1
    #Relatorio.
    print("nome:",nome)
    print("notas:",Nota1,Nota2,Nota3,Nota4)
    print("faltas:",faltas)
    print("media:",Media)
    print("Situacao:",situacao)
    cont = cont +1
print(Aluno)
   