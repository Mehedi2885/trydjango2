from django.contrib import admin
from .models import (Language, Framework, Movie, Character,
                     Language2, Framework2, Course, Section, Lecture)

# Register your models here.

admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Movie)
admin.site.register(Character)
admin.site.register(Language2)
admin.site.register(Framework2)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lecture)
