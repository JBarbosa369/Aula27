#cadastro de usuario e senha 
Saldo = 100 # variavel que guardará o saldo do usuario
while True:

    #menu principal
    print("Bem vindo! /n digite 1.cadastrar 2.login 3.encerrar")
    #ler a escolha principal
    menu = int(input()) #le a escolha 1

    #se usuario escolher cadastro
    if menu == 1:
        #cria um usuário e uma senha com tipo string
        usuario = input("crie um nome de usuario:")
        senha = input("crie uma senha:")
    elif menu == 2:
        #comparar as inf,cadastradas com uma leitura 
        login_usuario = input("digite seu usuario:")
        login_senha = input("digite sua senha:")
        if login_usuario == usuario and login_senha == senha:
            print("Login realizado com sucesso")
            #se login for correto,entra no 
            #menu principal do app
            print("bem vindo",usuario)
            while True:
                print("1.deposito 2.sacar 3.pix 4.xtrato 5.encerrar:")
                escolha_principal = int(input()) # se o usuario escolher depsito 
                if escolha_principal == 1:
                    #lê o valor a ser depositado
                    valor_deposito = float(input("DIGITE O VALOR DO DEPOSITO:"))
                    Saldo = Saldo + valor_deposito # atualiza o valor 
                    print("novo saldo",Saldo)
                elif escolha_principal == 2: # Saque
                    valor_saque = float(input("digite o valor do saque:"))
                    senha_saque = input(input("digite sua senha:"))
                    if senha_saque == senha: # se a senha for correta 
                        Saldo = Saldo - valor_saque # subtrai o valor do saldo
                    else:
                        print("senha incorreta")
                elif escolha_principal == 3: # se usuario escolher pix
                    valor_pix = float(input("digite o valor do pix:"))
                    senha_pix = input(("digite sua senha:"))
                    if senha_pix == senha:
                        Saldo = Saldo - valor_pix
                    else:
                        print("senha incorreta;")
                elif escolha_principal == 4: #se usuario escolher visualizar extrato
                    senha_extrato = input(("digite sua senha:"))
                    if senha_extrato == senha:
                        print("extrato",Saldo)
                    else:
                        print("senha incorreta")
                elif escolha_principal == 5:
                    senha_encerrar = input(("digite sua senha:"))
                    if senha_encerrar == senha:
                        break
                    else:
                        print("senha incorreta")
                

            
                

                    

    else:
         print("usuario ou senha incorreta")

