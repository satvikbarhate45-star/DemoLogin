from django.db import models

class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'registration'
        managed = False  # Django won't create or modify this table

    def __str__(self):
        return f"{self.first_name} {self.last_name}"