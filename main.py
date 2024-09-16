from datetime import datetime

def task_manager():
    tasks = []
    next_id = 1
    
    def add_task(title, due_date=None):
        nonlocal next_id
        task = {
            "id": next_id,
            "title": title,
            "status": "pendente",
            "created_at": datetime.now(),
            "due_date": datetime.strptime(due_date, '%Y-%m-%d') if due_date else None
        }
        tasks.append(task)
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

    def filter_by_due_date(due_date):
        due_date = datetime.strptime(due_date, '%Y-%m-%d')
        return [task for task in tasks if task['due_date'] and task['due_date'] <= due_date]

    def filter_by_creation_date(creation_date):
        creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
        return [task for task in tasks if task['created_at'] >= creation_date]

    def filter_overdue():
        current_date = datetime.now()
        return [task for task in tasks if task['due_date'] and task['due_date'] < current_date]

    # Função de alta ordem
    def apply_to_tasks(operation):
        return [operation(task) for task in tasks]

    # Exemplo de alta ordem: marcar todas as tarefas como concluídas
    def mark_all_as_done():
        apply_to_tasks(lambda task: task.update({"status": "concluída"}))

    return (add_task, get_tasks, remove_task, list_tasks, filter_pending, 
            mark_as_done, filter_by_due_date, filter_by_creation_date, filter_overdue, 
            apply_to_tasks, mark_all_as_done)
