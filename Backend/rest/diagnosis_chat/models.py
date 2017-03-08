from __future__ import unicode_literals
from django.db import models


class Main(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    discription = models.TextField()
    cause = models.TextField()
    treatment = models.TextField()
    def __str__(self):
        return self.name

    def __iter__(self):
        return [self.id,
                self.name,
                self.link,
                self.discription,
                self.cause,
                self.treatment,
               ]
    class Meta:
        managed = True
        db_table = 'main'


class Symptoms(models.Model):
    id = models.BigAutoField(primary_key=True)
    d_id = models.BigIntegerField()
    symptom = models.TextField()

    class Meta:
        managed = True
        db_table = 'symptoms'

class Userinput(models.Model):
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
