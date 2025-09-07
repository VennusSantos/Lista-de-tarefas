def adiconar_tarefa(lista_de_tarefas, tarefa):
    """adiciona tarefa à uma lista pré-existente"""
    lista_de_tarefas.append(tarefa)
    print(f"{'-' * 50} Tarefa adicionada com sucesso! ")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    """mostra as tarefas adicionadas na lista"""
    print("\n*" * 50)
    print(f"{' ' * 10} lista_de_tarefas")
    print("-" * 50)
    n = 1
    for tarefa in lista_de_tarefas:
        print(f" {n} - {tarefa}")
        n += 1
    print("-" * 50)

def excluir_tarefa(lista_de_tarefas, tarefa):
    """exclui uma tarefa da lista pré-existente a partir do número"""
    lista_de_tarefas.pop((tarefa - 1))
    return lista_de_tarefas

def exibir_menu():
    """mostra as opções da lista"""
    print("Escolha um opção:\n " \
    "1 - Adicionar Tarefa\n " \
    "2 - Listar Tarefas\n " \
    "3 - Excluir Tarefa\n " \
    "4 - Sair")

# Inicialização de variáveis
lista_de_tarefas = list()
continuar = True

# Cabeçalho do programa
print("-" * 50)
print("Bem vinde à sua lista de tarefas")
print("-" * 50)

# Loop principal
while continuar:
    exibir_menu()
    opção = input("Insira o que deseja fazer: ")
    if opção == "1":
        tarefa = input('Insira nova tarefa: ')
        lista_de_tarefas = adiconar_tarefa(lista_de_tarefas, tarefa) 
    elif opção == "2":
        listar_tarefas(lista_de_tarefas)
    elif opção == "3":
        tarefa = input('Insira o número da tarefa que deseja excluir')
        if not tarefa.isnumeric():
            print("Número inválido! Tente novamente: ")
        elif int(tarefa) >= len(lista_de_tarefas):
            print("Número inválido! Tente novamente: ")
        elif int(tarefa) <= 0:
            print("Número inválido! Tente novamente: ")
        else:
            excluir_tarefa(lista_de_tarefas, int(tarefa))
    elif opção == "4":
        continuar = False
    else:
        print("Opção invalida, tente novamente: ")
        print("\n")