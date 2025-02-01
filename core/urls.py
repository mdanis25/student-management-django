from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.StudentTemplateView.as_view(), name = 'homepage'), 
    path('create_student/', views.StudentCreateView.as_view(), name = 'create_student'),
    path('student_list/', views.StudentListView.as_view(), name = 'student_list'), 
    path('student_details/<int:pk>/', views.StudentDetailView.as_view(), name = 'student_details'), 
    path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name = 'update_student'),
    path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name = 'delete_student'), 
    
]
