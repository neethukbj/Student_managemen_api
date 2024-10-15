from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=50)
    enroll_date= models.DateTimeField()

    def __str__(self):
        return self.name
    

class Attendance(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    status=models.BooleanField()
    attendance_date=models.DateTimeField()

    def __str__(self):
        return f"{self.student.name}-{self.date}-{'Present' if self.status else 'absent'}"