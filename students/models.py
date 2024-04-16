from django.db import models

class Students(models.Model):

    student_name = models.CharField(max_length=200)

    student_college = models.CharField(max_length=200)

    student_avg = models.IntegerField()

    admission_date = models.DateTimeField()

    class Meta:

        ordering = ('student_name',)
