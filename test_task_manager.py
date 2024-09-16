import unittest
from datetime import datetime
from main import task_manager

class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        (self.add_task, self.get_tasks, self.remove_task, self.list_tasks, self.filter_pending, 
         self.mark_as_done, self.filter_by_due_date, self.filter_by_creation_date, 
         self.filter_overdue, self.apply_to_tasks, self.mark_all_as_done) = task_manager()

    def test_add_task(self):
        self.add_task("Estudar para prova", "2024-09-20")
        tasks = self.get_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], "Estudar para prova")
        self.assertEqual(tasks[0]['due_date'], datetime(2024, 9, 20))
    
    def test_remove_task(self):
        self.add_task("Finalizar projeto", "2024-09-15")
        self.remove_task(1)
        tasks = self.get_tasks()
        self.assertEqual(len(tasks), 0)

    def test_filter_pending(self):
        self.add_task("Comprar presentes", None)
        self.add_task("Estudar para prova", "2024-09-20")
        self.mark_as_done(2)
        pending_tasks = self.filter_pending()
        self.assertEqual(len(pending_tasks), 1)
        self.assertEqual(pending_tasks[0]['title'], "Comprar presentes")
    
    def test_filter_by_due_date(self):
        self.add_task("Finalizar projeto", "2024-09-15")
        self.add_task("Estudar para prova", "2024-09-20")
        filtered_tasks = self.filter_by_due_date("2024-09-18")
        self.assertEqual(len(filtered_tasks), 1)
        self.assertEqual(filtered_tasks[0]['title'], "Finalizar projeto")

    def test_filter_by_creation_date(self):
        self.add_task("Comprar presentes", None)
        self.add_task("Estudar para prova", "2024-09-20")
        filtered_tasks = self.filter_by_creation_date("2024-01-01")
        self.assertEqual(len(filtered_tasks), 2)

def test_filter_overdue(self):
    self.add_task("Finalizar projeto", "2024-09-15")
    self.add_task("Comprar presentes", "2024-09-20")

    overdue_tasks = self.filter_overdue()
    self.assertEqual(len(overdue_tasks), 1)
    self.assertEqual(overdue_tasks[0]['title'], "Finalizar projeto")


    def test_apply_to_tasks(self):
        self.add_task("Tarefa 1", None)
        self.add_task("Tarefa 2", "2024-09-20")
        titles = self.apply_to_tasks(lambda task: task["title"])
        self.assertEqual(titles, ["Tarefa 1", "Tarefa 2"])

    def test_mark_all_as_done(self):
        self.add_task("Tarefa 1", None)
        self.add_task("Tarefa 2", "2024-09-20")
        self.mark_all_as_done()
        tasks = self.get_tasks()
        self.assertTrue(all(task["status"] == "concluída" for task in tasks))

if __name__ == '__main__':
    unittest.main()
