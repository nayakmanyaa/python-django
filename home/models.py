from django.db import models


# makemigrations -> create changes and store in a file
# migrate - apply the pending changes created by makemigration


# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=125)
    lastname = models.CharField(max_length=125)
    email = models.CharField(max_length=125)
    mobile = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('P', 'Princess'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    about = models.TextField(max_length=125)
    date = models.DateField()
    
    # jisne contact add kiya hai, uska naam display hoga
    def __str__(self):
        return self.name