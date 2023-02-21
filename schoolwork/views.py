from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm, ClassForm, EditStudentForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as loginFun, logout
from .models import *
from django.contrib.auth.decorators import login_required

from datetime import datetime



def homepage(r):
    return render(r,"index.html") 

def applyForAdmission(r):
    form = StudentForm(r.POST or None, r.FILES or None)
    if r.method =="POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)
        else:
            return redirect(applyForAdmission)
    return render(r,"apply.html",{"form":form})

def login(r):
    LoginForm = AuthenticationForm(r, data=r.POST or None)

    if r.method =="POST":
        if LoginForm.is_valid():
            username = LoginForm.cleaned_data.get('username')
            password = LoginForm.cleaned_data.get('password')

            user = authenticate(username=username,password=password)

            if user is not None:
                print(user)
                loginFun(r, user)
                return redirect(homepage)
            else:
                return redirect(login)
                
    return render(r,"login.html",{"form":LoginForm})

def logoutFunction(r):
    logout(r)
    return redirect(login)


@login_required()
def manageStudents(r):
    data = {}
    data['title'] = "Manage Students"
    data['students']  = Student.objects.filter(isApproved=True)
    return render(r,"admin/manageStudents.html",data)

@login_required()
def manageAdmission(r):
    data = {}
    data['title'] = "Manage Admissions"
    data['students']  = Student.objects.filter(isApproved=False)
    return render(r,"admin/manageStudents.html",data)

@login_required()
def deleteStudent(r,id):
    std = Student.objects.get(pk=id)
    std.delete()
    return redirect(manageStudents)

@login_required()
def editStudent(r, id):
    std = Student.objects.get(pk=id)
    form = EditStudentForm(r.POST or None,r.FILES or None, instance=std)

    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(manageStudents)

    return render(r, "admin/editStudent.html", {"form":form})

@login_required()
def viewStudent(r, id):
    student = Student.objects.get(pk=id) 
    payments = Payment.objects.filter(student=student)
    return render(r, "admin/viewStudent.html",{"student":student, "payments":payments})

@login_required()
def approve(r, id):
    student = Student.objects.get(id=id, isApproved=False)
    currentMonth = datetime.now().month
    for month in range(currentMonth-1, 12):
        p = Payment()
        p.student = student
        p.month = MONTHS[month][0]
        p.amount = 800
        p.save()

    student.isApproved = True 
    student.save()
    return redirect(manageStudents)


@login_required()
def manageClasses(r):
    form = ClassForm(r.POST or None)
    data = {}
    data['title'] = "Manage Classes"
    data['form'] = form 
    data['classes'] = Classes.objects.all()

    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(manageClasses)
            
    return render(r, "admin/manageClasses.html",data)

@login_required()
def deleteClasses(r,id):
    classRecord = Classes.objects.get(pk=id)
    classRecord.delete()
    return redirect(manageClasses)

@login_required()
def viewClassWise(r, className):
    data = {}
    data["title"] = "Manage " + className + " class students"
    data['students'] = Student.objects.filter(className__className = className, isApproved=True)
    return render(r, "admin/manageStudents.html", data)


def scanRfCode(r):
    code = r.GET.get('code')
    try:
        student = get_object_or_404(Student,rf_code=code)
        return redirect(viewStudent,student.id)
    except:
        return redirect(manageStudents)

