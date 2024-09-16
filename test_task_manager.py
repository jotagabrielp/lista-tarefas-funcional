import unittest
from datetime import datetime
from main import task_manager

class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        (self.add_task, self.get_tasks, self.remove_task, self.list_tasks, self.filter_pending, 
         self.mark_as_done, self.filter_by_due_date, self.filter_by_creation_date, 
         self.filter_overdue, self.sort_tasks_by, self.filter_tasks_by_title, 
         self.mark_all_as_done, self.remove_done_tasks) = task_manager()

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
        self.add_task("Comprar presentes", "2024-09-10")
        overdue_tasks = self.filter_overdue()
        self.assertEqual(len(overdue_tasks), 1)
        self.assertEqual(overdue_tasks[0]['title'], "Comprar presentes")

    def test_sort_tasks_by_due_date(self):
        self.add_task("Estudar para prova", "2024-09-20")
        self.add_task("Finalizar projeto", "2024-09-15")
        sorted_tasks = self.sort_tasks_by("due_date")
        self.assertEqual(sorted_tasks[0]['title'], "Finalizar projeto")
        self.assertEqual(sorted_tasks[1]['title'], "Estudar para prova")
    
    def test_filter_tasks_by_title(self):
        self.add_task("Estudar para prova", "2024-09-20")
        self.add_task("Finalizar projeto", "2024-09-15")
        filtered_tasks = self.filter_tasks_by_title("projeto")
        self.assertEqual(len(filtered_tasks), 1)
        self.assertEqual(filtered_tasks[0]['title'], "Finalizar projeto")
    
    def test_mark_all_as_done(self):
        self.add_task("Comprar presentes", None)
        self.add_task("Estudar para prova", "2024-09-20")
        self.mark_all_as_done()
        tasks = self.get_tasks()
        for task in tasks:
            self.assertEqual(task['status'], "concluída")

    def test_remove_done_tasks(self):
        self.add_task("Comprar presentes", None)
        self.add_task("Estudar para prova", "2024-09-20")
        self.mark_as_done(1)
        self.remove_done_tasks()
        tasks = self.get_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], "Estudar para prova")
    
if __name__ == '__main__':
    unittest.main()
