from django.forms import ModelForm,Form,CharField,PasswordInput
from .models import Student,Classes

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ("isApproved","rf_code")


class EditStudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ("isApproved",)

class ClassForm(ModelForm):
    class Meta:
        model = Classes
        fields = "__all__"