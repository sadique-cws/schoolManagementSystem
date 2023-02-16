from django.forms import ModelForm,Form,CharField,PasswordInput
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ("isApproved",)

# class LoginForm(Form): 
#     username = CharField(max_length=200)
#     password = CharField(max_length=200,widget=PasswordInput())

