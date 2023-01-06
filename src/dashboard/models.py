from django.db import models
import datetime
from users.models import Users
from dataclasses import dataclass

# Create your models here.
class Diary(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(default="")
    date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"
    

class DiaryORM:

    @dataclass
    class Schema:
        user: Users
        title: str
        content: str
        date: str
    

    def insert(self, data: Schema) -> None:
        instance = Diary()
        instance.user = data.get("user")
        instance.title = data.get('title')
        instance.content = data.get('content')
        instance.date = data.get('date')
        instance.save()

    def get(self, id):
        try:
            diary = Diary.objects.get(pk=id)
        except Diary.DoesNotExist:
            diary = False
        return diary
    
    def user_diary(self , user):
        
        diarys = Diary.objects.filter(user=user).all()
        return diarys
    
    

