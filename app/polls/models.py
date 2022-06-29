from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# This is how we can create a new table inside of our table
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date publish")

    # Here I do a little bit of operator ovearloding 
    def __str__(self) -> str:
        return self.question_text

    def was_recent(self) -> bool:
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=7)
    
# This is another table 
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
