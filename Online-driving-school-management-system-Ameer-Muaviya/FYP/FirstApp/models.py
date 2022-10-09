from django.db import models



class Students(models.Model):
    username = models.CharField(max_length=34)
    phone = models.CharField(max_length=34)
    address = models.TextField(max_length=34)
    email = models.TextField(max_length=34)
    age = models.IntegerField()
    gender = models.TextField(max_length=10)
    vehicle = models.TextField(max_length=25)
    time = models.TextField(max_length=25)
    profile_pic =models.ImageField(upload_to='profile',null=True,blank=True,default='media/default/profile.jpg')

class Attendence(models.Model):
    username = models.CharField(max_length=34)
    date=models.DateField( auto_now_add=False)
    status=models.CharField(max_length=10)

class Programs(models.Model):
    program_name=models.CharField(max_length=25)    
    summary=models.TextField(max_length=500)
    vehicle=models.CharField(max_length=25, unique=True)
    instructor=models.CharField(max_length=25 ,unique=True)

class Notifications(models.Model):
    date=models.DateTimeField(blank=True)
    username = models.CharField(max_length=34)
    message=models.TextField(max_length=500)

class Assignments(models.Model):
    name = models.CharField(max_length=34)
    username = models.CharField(max_length=34)
    file=models.FileField(upload_to='assignments/', max_length=100)

class SubmitAssignment(models.Model):
    date=models.DateTimeField()
    username = models.CharField(max_length=34)
    state = models.CharField(max_length=34)
    file=models.FileField(upload_to='submittedAssignmets/', max_length=100)

class ManageVehicles(models.Model):
    name=models.CharField(max_length=50,unique=True)
    number=models.IntegerField( unique=True)
    fee=models.IntegerField()

class Instructor(models.Model):
    name=models.CharField(max_length=50)
    number=models.IntegerField(unique=True)
    experience=models.CharField(max_length=50)
    sallary=models.IntegerField()

class Links(models.Model):
    username=models.CharField(max_length=50)
    link=models.CharField(max_length=50)
    
