from django.db import models
from django.contrib.auth.models import User

# -----------------------------
# Profile Model: All Users
# -----------------------------
class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('director', 'Director'),
        ('librarian', 'Librarian'),
        ('janitor', 'Janitor'),
        ('counselor', 'Counselor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# -----------------------------
# Student Model
# -----------------------------
class Student(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)  # e.g., 10, 11, 12
    classroom = models.ForeignKey('Classroom', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.profile.user.username} - Grade {self.grade}"


# -----------------------------
# Teacher Model
# -----------------------------
class Teacher(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.profile.user.username} - {self.department}"


# -----------------------------
# Classroom Model
# -----------------------------
class Classroom(models.Model):
    name = models.CharField(max_length=50)  # e.g., "Grade 11 Science"
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


# -----------------------------
# Assignment Model
# -----------------------------
class Assignment(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.classroom.name}"


# -----------------------------
# Other Staff Models
# -----------------------------
class Director(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    office_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.profile.user.username} - Director"


class Librarian(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    library_section = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.profile.user.username} - Librarian"
