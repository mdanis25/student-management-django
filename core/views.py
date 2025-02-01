from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib import messages
from core.models import StudentModel 
from core.forms import StudentModelForm


class StudentTemplateView(TemplateView): 
    template_name = 'home.html'


class StudentListView(ListView):  
    model = StudentModel
    template_name = 'students/student_list.html' 
    context_object_name = 'students' 
    
class StudentDetailView(DetailView): 
    model = StudentModel
    template_name = 'students/student_details.html' 
    context_object_name = 'student' 
    pk_url_kwarg = 'pk'  
    
class StudentCreateView(CreateView): 
    model = StudentModel 
    form_class = StudentModelForm
    template_name = 'students/student_register.html' 
    success_url = reverse_lazy('student_list')  
    
    def form_valid(self, form): 
        messages.success(self.request, 'Student added successfully!')
        return super().form_valid(form) 
    
    
class StudentUpdateView(UpdateView): 
    model = StudentModel 
    form_class = StudentModelForm
    template_name = 'students/student_register.html' 
    success_url = reverse_lazy('student_list') 
    
    def form_valid(self, form):
        messages.success(self.request, 'Student updated successfully!')
        return super().form_valid(form)
    
class StudentDeleteView(DeleteView): 
    model = StudentModel 
    template_name = 'students/student_delete_confrim.html' 
    success_url = reverse_lazy('student_list') 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.get_object()   
        context['student'] = student  
        return context
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Student record deleted successfully!')
        return super().delete(request, *args, **kwargs)