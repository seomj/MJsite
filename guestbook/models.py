from django.db import models


class Guestbook(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    contents = models.TextField(null=False)
    reg_date = models.DateTimeField(auto_now=True)