from django.db import models


class Idol(models.Model):
    name = models.CharField(max_length=100)
    member = models.ManyToManyField('Member')
    ent = models.ManyToManyField('Ent')
    youtube = models.URLField()
    more = models.URLField()

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=10)
    birth = models.DateField()
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Ent(models.Model):
    name = models.CharField(max_length=30)
    website = models.URLField("Site URL")

    def __str__(self):
        return self.name
