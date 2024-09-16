from datetime import datetime

def task_manager():
    tasks = []
    next_id = 1
    
    def add_task(title, due_date=None):
        nonlocal next_id
        creation_date = datetime.now()
        if due_date:
            due_date = datetime.strptime(due_date, "%Y-%m-%d")
        tasks.append({
            "id": next_id,
            "title": title,
            "status": "pendente",
            "creation_date": creation_date,
            "due_date": due_date
        })
        next_id += 1
        return tasks
    
    def get_tasks():
        return tasks
    
    def remove_task(task_id):
        nonlocal tasks
        tasks = list(filter(lambda task: task["id"] != task_id, tasks))
        return tasks

    def list_tasks():
        return [
            f"ID: {task['id']} | Título: {task['title']} - Status: {task['status']} - Data Criação: {task['creation_date'].strftime('%Y-%m-%d')} - Data Limite: {task['due_date'].strftime('%Y-%m-%d') if task['due_date'] else 'Sem data limite'}"
            for task in tasks
        ]

    def filter_pending():
        return [task for task in tasks if task["status"] == "pendente"]

    def mark_as_done(task_id):
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "concluída"
        return tasks

    def filter_by_due_date(before_date=None):
        if before_date:
            before_date = datetime.strptime(before_date, "%Y-%m-%d")
            return [task for task in tasks if task["due_date"] and task["due_date"] < before_date]
        return []

    def filter_by_creation_date(after_date=None):
        if after_date:
            after_date = datetime.strptime(after_date, "%Y-%m-%d")
            return [task for task in tasks if task["creation_date"] and task["creation_date"] > after_date]
        return []

    def filter_overdue():
        current_date = datetime.now()
        return [task for task in tasks if task['due_date'] and task['due_date'] < current_date]

    def sort_tasks_by(key="creation_date"):
        if key == "due_date":
            return sorted(tasks, key=lambda task: (task["due_date"] is None, task["due_date"]))  # Tarefas sem data limite no final
        elif key == "title":
            return sorted(tasks, key=lambda task: task["title"].lower())  # Ordena por título em ordem alfabética
        return sorted(tasks, key=lambda task: task["creation_date"])  # Ordena por data de criação por padrão

    def filter_tasks_by_title(substring):
        return list(filter(lambda task: substring.lower() in task["title"].lower(), tasks))

    def mark_all_as_done():
        list(map(lambda task: task.update({"status": "concluída"}), tasks))
        return tasks

    def remove_done_tasks():
        nonlocal tasks
        tasks = list(filter(lambda task: task["status"] != "concluída", tasks))
        return tasks

    return (add_task, get_tasks, remove_task, list_tasks, filter_pending, mark_as_done, 
            filter_by_due_date, filter_by_creation_date, filter_overdue, sort_tasks_by, 
            filter_tasks_by_title, mark_all_as_done, remove_done_tasks)

