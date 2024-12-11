#Declarar uma funçao.
def Saudacoes(hora_do_dia): # exibir a saudação correspondente a hora.
# dar bom dia 
    if (hora_do_dia >= 0) and (hora_do_dia <= 12):
        print("bom dia")
    elif (hora_do_dia>= 13) and (hora_do_dia <= 18):
      print("Boa tarde")

#Fora da função
resposta = int(input("digite que horas são:"))

Saudacoes(resposta)

