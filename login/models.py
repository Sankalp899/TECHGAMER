from unicodedata import name
from django.db import models

# Create your models here.

#Create a contact model in database

#create class
class Contact(models.Model):   
#adding an argument primary_key=True to AutoField will make it primary key for that table in relational database.    
    sno = models.AutoField(primary_key = True)    
#The maximum length (in characters) of the field. The max_length is enforced at the database level and in Django’s validation  
    name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 13)
    email = models.CharField(max_length = 100)
    query = models.TextField()

    def __str__(self):
        return 'Message from '+self.name+' '+self.email

############################################################################
#Create a Games model in database

#create class
class Playgame(models.Model):
    
# file will be uploaded to MEDIA_ROOT /images
    image = models.ImageField(upload_to='images',default=None)

#The maximum length (in characters) of the field. The max_length is enforced at the database level and in Django’s validation
    name = models.CharField(max_length=50)
    game = models.CharField(max_length=250)
    def __str__(self):
        return self.name

##############################################################################
#Create a Download model in database

#create class

class Download(models.Model):
    game = models.FileField(upload_to='media')
    image = models.ImageField(upload_to='images',default=None)
    name = models.CharField(max_length=50)
    def __str__(self):
        
        return self.title