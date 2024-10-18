from django.db import models
from category.models import CategoryModel

# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.CharField(max_length=400)
    is_Completed = models.BooleanField(default=False)
    assign_date = models.DateField()
    categories = models.ManyToManyField(CategoryModel, related_name='tasks')  

    def __str__(self):
        return self.task_title
