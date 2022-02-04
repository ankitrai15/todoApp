from django.db import models

class todoList(models.Model):
    item_name = models.CharField(max_length=20)
