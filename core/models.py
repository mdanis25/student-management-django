from django.db import models

class StudentModel(models.Model):  
    class CourseChoice(models.TextChoices): 
        MATH = 'Math', 'Math',
        ENGLISH = 'English', 'English', 
        HISTORY = 'History', 'History', 
        SICENCE = 'Science', 'Science',
        PHYSICES = 'Physices', 'Physices' 
        
    id = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=254) 
    phone = models.CharField(max_length=11) 
    course = models.CharField(max_length=100, choices = CourseChoice.choices, default = CourseChoice.SICENCE) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    
    
    def __str__(self): 
        return self.name 