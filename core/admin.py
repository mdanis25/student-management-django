from django.contrib import admin
from core.models import StudentModel

@admin.register(StudentModel) 
class AdminStudentModel(admin.ModelAdmin): 
    list_display = ['id', 'name', 'email', 'phone', 'course', 'created_at', 'updated_at']