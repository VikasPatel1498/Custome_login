from django.db import models

# Create your models here.
class Member(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self/firstname+""+self.lastname
    
    class Meta:
        db_table = 'web_member'

    