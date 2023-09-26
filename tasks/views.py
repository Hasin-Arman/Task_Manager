from django.shortcuts import render,redirect
from .forms import TaskForm
from django.utils.text import slugify
from .models import taskModel
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializers import TaskSerializer
from django.db.models import Q


class Task_Form_view(FormView):
   template_name='add_task.html'
   form_class=TaskForm
   success_url=reverse_lazy('profile')
   
   def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.priority_slug=slugify(form.cleaned_data['priority'])
        form.save()
        return super().form_valid(form)
    
class TaskListView(ListView):
   model=taskModel
   template_name='profile.html'
   context_object_name='tasks'
   
   def get_queryset(self):
      return taskModel.objects.filter(user=self.request.user)
   
    
class TaskDetailsView(DetailView):
   model=taskModel
   template_name='task_details.html'
   context_object_name='task'
   pk_url_kwarg='id'
   success_url=reverse_lazy('completed_task_list')
   
   
class task_Update_View(UpdateView):
   model=taskModel
   template_name='add_task.html'
   form_class=TaskForm
   success_url=reverse_lazy('profile')
   
class Task_Delete_View(DeleteView):
   model=taskModel
   template_name='del_conf.html'
   success_url=reverse_lazy('profile')

def completeView(request,id):
   item = taskModel.objects.get(id=id)
   item.is_complete = True
   item.save()
   return redirect('show_complete')

def searchView(request):
   value=request.POST.get('value')
   data=taskModel.objects.filter(title=value)
   return render(request,'profile.html',{'tasks':data})

def completedTasks(request):
   data=taskModel.objects.filter(is_complete=True)
   return render(request,'profile.html',{'tasks':data})
   
def priorityFilter(request,PrioritySlug):
   if PrioritySlug:
      data=taskModel.objects.filter(priority_slug=PrioritySlug)
   else:
      data=data=taskModel.objects.all()
   print(data)
   return render(request,'profile.html',{'tasks':data})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = taskModel.objects.all()
    serializer_class = TaskSerializer
    

class ShowCompletedTasks(ListView):
   model=taskModel
   template_name='completed_task.html'
   context_object_name='tasks'
   
   def get_queryset(self):
      return taskModel.objects.filter(Q(is_complete=True) & Q(user=self.request.user))