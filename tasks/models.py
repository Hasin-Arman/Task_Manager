from django.db import models
from django.contrib.auth.models import User
# Create your models here.
PRIORITY=(
    ('Low','Low'),
    ('Medium','Medium'),
    ('High','High'),
)
class taskModel(models.Model):
    user=models.ForeignKey(User, related_name='task', on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300,null=True, blank=True)
    photo=models.ImageField(upload_to="img/")
    creation_date=models.DateTimeField(auto_now_add=True)
    due_date=models.DateField()
    priority=models.CharField(max_length=100,choices=PRIORITY)
    priority_slug=models.SlugField(max_length=100,null=True,blank=True)
    is_complete=models.BooleanField(default=False)
    
    