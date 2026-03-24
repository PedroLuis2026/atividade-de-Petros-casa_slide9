import os
os.system("cls" if os.name == "nt" else "clear")

verde = "\033[32m"
vermelho = "\033[31m"
amarelo = "\033[33m"
reset = "\033[m"

tarefas = []
tarefas_concluidas = []
escolha = 0
while True:
    print(f"{"MENU":=^34}")
    print("1. Criar tarefas")
    print("2. Listar tarefas")
    print("3. Marcar conclusão da tarefa")
    print("4. Listar tarefas concluidas")
    print("5. Sair do programa")
    print(f"{len(tarefas_concluidas)} Tarefas foram concluidas")
    print("=" * 30)
    try:
        escolha = int(input("Digite a opção que você deseja: (apenas as númerações) "))
        if escolha not in [1, 2, 3, 4, 5]:
            print(f"{vermelho}Erro! Opção inexistente.{reset}")
            continue
    except ValueError:
        print(f"{vermelho}APENAS NÚMEROS!{reset}")
        continue
    if escolha == 1:
        criar = input("Digite a tarefa que você quer fazer: ")
        tarefas.append(criar)
        print(f"{verde}Tarefa adicionada!^{reset}")
        print("=" * 30)
        continue
    if escolha == 2:
        print(f"{"TAREFAS":=^37}")
        if len(tarefas) == 0:
            print(f"{amarelo}Nenhuma tarefa para ser listada.{reset}")
            print("=" * 30)
        else:
            for i, v in enumerate(tarefas, 1):
                print(f"{i}°. {amarelo}{v}{reset}")
            print("=" * 30)
        continue
    if escolha == 3:
        if len(tarefas) == 0:
            print(f"{amarelo}Nenhuma tarefa para ser concluída.{reset}")
            print("=" * 30)
            continue
        else:
            try:
                concluir = int(input("Digite qual tarefa você quer concluir: "))
                idx = concluir - 1 
                if 0 <= idx < len(tarefas):
                   deletada = tarefas.pop(idx)#Tarefa saindo de pendente para concluida
                   concluida = tarefas_concluidas.append(deletada)#Nova tarefa concluida
                   print(f"A tarefa {verde}{deletada}{reset} foi concluida com sucesso")
                   print("=" * 30)
                   continue
                else:
                    print(f"{vermelho}Número inválido!{reset}")
            except ValueError:
                print(f"{vermelho}APENAS DIGITE NÚMEROS!{reset}")
                print("=" * 30)
                continue
    if escolha == 4:
        print(F"{"TAREFAS CONCLUIDAS":=^48}")
        if len(tarefas_concluidas) == 0:
            print(f"{amarelo}Nenhuma tarefa foi concluida.{reset}")
            print("=" * 30)
        else:
            for i,t in enumerate(tarefas_concluidas, 1):
                print(f"{i}°. {verde}{t}{reset}")
    if escolha == 5:
        while True:
            escolha_final = input("Você tem certeza que quer sair? [S/N] ").upper().strip()
            if escolha_final not in "SN":
                print("Escolha apenas entre S (sim) ou N (não)")
                continue
            break
        if escolha_final == "N":
            continue
        else:
            print("-=-" * 10)
            break
print("👋Até mais!")
print("-=-" * 10)
            
