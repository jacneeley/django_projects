import datetime
from django.db import models
from django.utils import timezone

# layout for the database

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def was_published_recently(this):
        return this.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(this): #I like using 'this', ok?
        return this.question_text

class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(this):
        return this.choice_text

#Remember the 3 step guide to making model changes

## change your models here (models.py)
## run python manage.py makemigrations to apply those changes to the DB
## run pythong manage.py migrate to apply changes to the DB