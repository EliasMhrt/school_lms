from django.contrib import admin
from .models import (
    Profile, Student, Teacher, Classroom, Assignment,
    Director, Librarian
)

# Register all models to admin
admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Assignment)
admin.site.register(Director)
admin.site.register(Librarian)
