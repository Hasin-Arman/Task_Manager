from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet,basename="task")

urlpatterns =[
    path('api/', include(router.urls)),
    path('add-task/',views.Task_Form_view.as_view(),name='add'),
    path('profile/',views.TaskListView.as_view(),name='profile'),
    path('details/<int:id>/',views.TaskDetailsView.as_view(),name='details'),
    path('update/<int:pk>/',views.task_Update_View.as_view(),name='update'),
    path('delete/<int:pk>/',views.Task_Delete_View.as_view(),name='delete'),
    path('complete/<int:id>/',views.completeView,name='complete'),
    path('search/',views.searchView,name='search'),
    path('task_complete/',views.completedTasks,name='task_complete'),
    path('priority/<slug:PrioritySlug>/',views.priorityFilter,name='priority'),
    path('show_complete/',views.ShowCompletedTasks.as_view(),name='show_complete'),
]