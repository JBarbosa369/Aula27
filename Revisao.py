#Ler entradas do usuario.
#o codigo lendo varios alunos e a mesma coisa
#a unica diferença é que ele está dentro de uma repetição 
 #variavel que controla a repetição.
Alunos = []#lista que guardará todos os dados dos alunos cadastrado.
while True:
    Menu = int (input()) # variavel que guarda qual escolha do usuario.
    
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
            cont = cont +1
    #enviar os dados do aluno para a lista alunos
            Alunos.append([nome,faltas,Media,situacao])
       
        
    elif Menu == 2:#Relatorio.
     Alunos.append([nome,faltas,Media,situacao])
     cont =+ 1
     print(Alunos)

    elif Menu == 3: # se o usuario escolher encerrar.
        break # quebra a execução do enquanto.



   