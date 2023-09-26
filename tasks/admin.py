from django.contrib import admin
from .models import taskModel
# Register your models here.

class taskAdminModel(admin.ModelAdmin):
    list_display=['title','due_date','priority','is_complete']
    ordering=['priority']
    
admin.site.register(taskModel,taskAdminModel)
    