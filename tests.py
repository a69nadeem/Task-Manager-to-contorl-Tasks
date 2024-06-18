# tasks/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create_user(username='testuser', password='12345')
        Task.objects.create(title='Sample Task', description='This is a sample task.', created_by=User.objects.get(username='testuser'))

    def test_task_creation(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.title, 'Sample Task')
        self.assertEqual(task.description, 'This is a sample task.')
        self.assertFalse(task.completed)
