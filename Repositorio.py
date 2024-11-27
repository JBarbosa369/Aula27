calcular_situacao(media, faltas):
imite_faltas = 25
media_aprovacao = 7
media_recuperacao = 5

if faltas > limite_faltas:
    return "Reprovado por faltas"
elif media >= media_aprovacao:
    return "Aprovado"
elif media >= media_recuperacao:
    return "Recuperação"
else:
return "Reprovado por nota"

alunos = []
print("=== Cadastro de Alunos ===")
while True:
        nome = input("Nome do aluno (ou 'fim' para terminar): ").strip()
        if nome.lower() == 'fim':
            break

        try:
            nota1 = float(input(f"Digite a 1ª nota de {nome}: "))
            nota2 = float(input(f"Digite a 2ª nota de {nome}: "))
            faltas = int(input(f"Digite o número de faltas de {nome}: "))
        except ValueError:
            print("Por favor, insira valores válidos.")
            continue

        media = (nota1 + nota2) / 2
        situacao = calcular_situacao(media, faltas)

        alunos.append({
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2,
            "faltas": faltas,
            "media": media,
            "situacao": situacao
        })

print(alunos)

exibir_relatorio(alunos)
print("\n=== Relatório Final ===")
print(f"{'Nome':<20}{'Nota 1':<10}{'Nota 2':<10}{'Faltas':<10}{'Média':<10}{'Situação':<20}")
print("=" * 80)
for aluno in alunos:
        print("{aluno['nome']:<20}{aluno['nota1']:<10.2f}{aluno['nota2']:<10.2f}{aluno['faltas']:<10}"
              "{aluno['media']:<10.2f}{aluno['situacao']:<20}")

def main():
    """
    Função principal do programa.
    """
    alunos = coletar_dados_alunos()
    exibir_relatorio(alunos)

if __name__ == "__main__":
    main()

