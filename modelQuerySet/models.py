from django.db import models

# Create your models here.

"""Many to one/ One to many/ Parent-Child relationship"""


class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=20)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


"""Another one to many/many to one"""


class Course(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return self.title


class Lecture(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    code_link = models.CharField(max_length=100, blank=True)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.title


"""End many to one"""

"""One to one"""


class Language2(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Framework2(models.Model):
    name = models.CharField(max_length=20)
    language = models.OneToOneField(Language2, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


""""End one to one"""

"""Many to many"""


class Movie(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=20)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name


"""End many to many"""
