from django.db import models

# Create your models here.

class User(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    ]
    name = models.CharField(max_length=100) 
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'instructor'})

    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)    
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)   
    def __str__(self):
        return f"{self.student.name} - {self.course.name}"
class EnrollmentItem(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='items')
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    completion_status = models.BooleanField(default=False)

    def __str__(self):
        return self.enrollment.student.name + ' - ' + self.enrollment.course.name + ' - ' + str(self.progress) + '%'      