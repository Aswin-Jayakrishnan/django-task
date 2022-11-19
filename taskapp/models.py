from django.db import models

# Create your models here.



class login(models.Model):
    uname = models.CharField(max_length=100)
    pswd = models.CharField(max_length=100)
    utype = models.CharField(max_length=100)



class admin(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.BigIntegerField()
    image = models.FileField()
    login_id = models.ForeignKey(login,on_delete=models.CASCADE)


class student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.BigIntegerField()
    image = models.FileField()
    login_id = models.ForeignKey(login, on_delete=models.CASCADE)


class mark(models.Model):
    subject = models.CharField(max_length=100)
    mark = models.CharField(max_length=100)
    stud_id = models.ForeignKey(student, on_delete=models.CASCADE)