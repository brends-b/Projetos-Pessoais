#Cadastro de Alunos
#Descrição:
# > menu com opções de navegação 
# > armazenar, atualizar e exibir nomes e notas de alunos,
# > calcular a média geral da turma,
# > destacar quem foi aprovado (nota ≥ 7) e quem foi reprovado.

alunos = [{'nome':'bel', 'nota': 10}]

while True:

    print("\n--- SIGAA ---\n")
    
    if not alunos:
        print(f"Nenhum aluno cadastrado")
    else:
        nomes_cadastrados = [a['nome'].capitalize() for a in alunos]
        print(f"Alunos cadastrados: {', '.join(nomes_cadastrados)}")

    print("\nDIGITE UMA OPÇÃO:")
    print(" 1 - Cadastrar Aluno(a)")
    print(" 2 - Cadastrar Nota")
    print(" 3 - Exibir Notas")
    print(" 4 - Média da Turma")
    print(" 5 - Stats (Aprovados/Reprovados)")
    print(" 6 - Excluir aluno(a)")
    print(" 0 - Sair \n")

    try:
        opcao = int(input("Opção: "))

    except ValueError:
        print(f"\nDigite um número válido")
        continue

    if opcao == 0:
            break

    elif opcao == 1:
        aluno_existe = False
        aluno = input("\nNome do aluno(a): ").lower()

        for a in alunos:
            if a['nome'] == aluno:
                aluno_existe = True
                break

        if aluno_existe == True:
            print("\nAluno(a) já cadastrado")
        else:
            novo_aluno = {'nome': aluno, 'nota': None}
            alunos.append(novo_aluno)
            print(f"\nAluno(a) {aluno.capitalize()} cadastrado com sucesso!")

    elif opcao == 2:
        aluno_existe = False
        aluno = input("\nAluno(a): ").lower()

        for a in alunos:
            if a['nome'] == aluno:
                aluno_existe = True
                nota = float(input("\nNota: "))
                a['nota'] = nota
                print("\nNota atualizada com sucesso!")
                break

        if aluno_existe == False:
            print("\nAluno(a) não encontrado. Realize o cadastro")

    elif opcao == 3:
        aluno_existe = False
        aluno = input("\nDigite o aluno(a) a ser exibido: ").lower()

        for a in alunos:
            if a['nome'] == aluno:
                aluno_existe = True
                print(f"\nNome: {a['nome'].capitalize()} \nNota: {a['nota']}")
                break
        
        if aluno_existe == False:
            print(f"\nO aluno(a) {aluno.capitalize()} não está cadastrado")

    elif opcao == 4:
        
        if len(alunos) == 0:
            print("\nNão há alunos cadastrados")
        else:
            soma = 0 
            alunos_com_nota = 0

            for a in alunos:
                if a['nota'] is not None:
                    soma += float(a['nota'])
                    alunos_com_nota += 1
                    
            if alunos_com_nota == 0:
                print("\nCadastre uma nota antes de verificar a média")
            else:            
                media = soma/alunos_com_nota
                print(f"\nMédia Global dentre {alunos_com_nota} alunos: {media:.2f}")
                    
    elif opcao == 5:
        
        if not alunos:
            print("\nNão há alunos cadastrados")
        else:
            barema = float(input("\nDigite a média para aprovação: "))
            aprovados = []
            reprovados = []
            alunos_sem_nota = []

            for a in alunos:
                if a['nota'] is not None:
                    if float(a['nota']) >= barema:
                        aprovados.append(a)
                    else:
                        reprovados.append(a)
                else:
                    alunos_sem_nota.append(a)

            if not aprovados and not reprovados:
                print(f"\nCadastre alguma nota antes de verificar as estatísticas")
            else:
                print(f"\nAprovados ({len(aprovados)})")
                for a in aprovados:
                    print(f"- {a['nome'].capitalize()}: {a['nota']}")
                print(f"\nReprovados ({len(reprovados)})")
                for a in reprovados:
                    print(f"- {a['nome'].capitalize()}: {a['nota']}")
                print(f"\nAlunos sem nota cadastrada: {len(alunos_sem_nota)}")

    elif opcao == 6:
        aluno_existe = False
        aluno = input("\nDigite o aluno(a) que deseja excluir: ").lower()

        for a in alunos.copy():
            if a['nome'] == aluno:
                aluno_existe = True
                alunos.remove(a)
                print(f"\nAluno(a) {aluno.capitalize()} excluído do banco de dados")
                break
        
        if not aluno_existe:
            print("\nEste aluno(a) já não existe")

    else:
        print("\nDigite um número válido")