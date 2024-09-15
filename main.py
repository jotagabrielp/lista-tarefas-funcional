def task_manager():
    tasks = []
    next_id = 1
    
    def add_task(title):
        nonlocal next_id
        tasks.append({"id": next_id, "title": title, "status": "pendente"})
        next_id += 1
        return tasks
    
    def get_tasks():
        return tasks
    
    def remove_task(task_id):
        nonlocal tasks
        tasks = list(filter(lambda task: task["id"] != task_id, tasks))
        return tasks

    def list_tasks():
        return [f"ID: {task['id']} | Título: {task['title']} - Status: {task['status']}" for task in tasks]

    def filter_pending():
        return [task for task in tasks if task["status"] == "pendente"]

    def mark_as_done(task_id):
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "concluída"
        return tasks

    return add_task, get_tasks, remove_task, list_tasks, filter_pending, mark_as_done

add_task, get_tasks, remove_task, list_tasks, filter_pending, mark_as_done = task_manager()


def main():
    while True:
        print("\n--- Gerenciamento de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Listar todas as tarefas")
        print("4. Filtrar tarefas pendentes")
        print("5. Marcar tarefa como concluída")
        print("6. Sair")
        
        choice = input("Escolha uma opção (1-6): ")

        if choice == '1':
            title = input("Digite o título da tarefa: ")
            add_task(title)
            print(f"Tarefa '{title}' adicionada com sucesso!")

        elif choice == '2':
            task_id = int(input("Digite o ID da tarefa que deseja remover: "))
            tasks = remove_task(task_id)
            print(f"Tarefa com ID '{task_id}' removida com sucesso!")

        elif choice == '3':
            print("\n--- Lista de Tarefas ---")
            tasks = get_tasks()
            if tasks:
                for task in list_tasks():
                    print(task)
            else:
                print("Nenhuma tarefa cadastrada.")

        elif choice == '4':
            print("\n--- Tarefas Pendentes ---")
            pending_tasks = filter_pending()
            if pending_tasks:
                for task in [f"ID: {task['id']} | Título: {task['title']} - Status: {task['status']}" for task in pending_tasks]:
                    print(task)
            else:
                print("Nenhuma tarefa pendente.")

        elif choice == '5':
            task_id = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
            tasks = mark_as_done(task_id)
            print(f"Tarefa com ID '{task_id}' marcada como concluída!")

        elif choice == '6':
            print("Saindo do sistema... Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
