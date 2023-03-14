from django.db import models
from uuid import uuid4


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=250, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
