from django.db import models

class Project(models.Model):
    subject = models.CharField(max_length = 250 , verbose_name = "subject" )
    end_day = models.DateField(editable = True, blank = True , null = True , verbose_name = "end day" )
    description = models.TextField(verbose_name = 'description ' ,default = '', blank = True)
    img = models.ImageField(upload_to='pics',blank = True)
    file = models.FileField(upload_to='files',blank = True)

class First(models.Model):
    header_text = models.CharField(max_length = 250 , verbose_name = "subject" ,default="", blank = True)
    first_back = models.ImageField(upload_to='pics')
