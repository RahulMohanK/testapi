from django.db import models

# Create your models here.
class Report_db(models.Model):
    Name = models.CharField(max_length=10)
    Phone = models.CharField(max_length=10)

    def __str__(self):
        return self.Name
