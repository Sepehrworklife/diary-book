from django.db import models
from users.models import Users

# Create your models here.
class Diary(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField
    date = models.DateTimeField
    created_date = models.DateTimeField(auto_now=True)
    