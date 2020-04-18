from django.db import models



class Member(models.Model):
    fname = models.CharField(max_length=50)
    memberid = models.CharField(max_length=50)
    password = models.CharField(max_length=50, blank=True)


class Todolist (models.Model):
    id = models.AutoField(primary_key=True)
    todos = models.CharField(max_length=50)
    memberid = models.ForeignKey('member', on_delete=models.CASCADE)
    todostatus = models.IntegerField(default=0)
    datecreated = models.DateTimeField(auto_now=True)
    datefinished = models.DateTimeField(auto_now=True)
    agreedbymom = models.IntegerField(default=0)
