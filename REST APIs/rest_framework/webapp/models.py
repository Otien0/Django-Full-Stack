from django.db import models

# Create your models here.
class employees(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    emp_id = models.IntegerField()
    jobtype = models.CharField(max_length=256)

    def __str__(self):
        return self.firstname + ' ' + self.lastname