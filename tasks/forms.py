from django import forms
from .models import taskModel
class TaskForm(forms.ModelForm):
    due_date= forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = taskModel
        exclude =['user','is_complete','priority_slug']
        
    
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs) 
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
    