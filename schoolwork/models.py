from django.db import models

# Create your models here.

GENDER  = (
    ("M","male"),
    ("F","Female"),
    ("O", "Other")
)

CLASSLIST = (
    ("LKG","LKG"),
    ("UKG","UKG"),
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
)

class Classes(models.Model):
    className = models.CharField(max_length=200,choices=CLASSLIST)

    def __str__(self):
        return self.className
    
class Student(models.Model):
    full_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10,choices=GENDER)
    nationality = models.CharField(max_length=20, choices=(("Indian","Indian"),("Other","Other")))
    address = models.TextField()
    city = models.CharField(max_length=30,choices=(("Purnea","Purnea"),("Bhagalpur","Bhagalpur")))
    state = models.CharField(max_length=200)
    pin_code = models.IntegerField()
    contact = models.CharField(max_length=15)
    image = models.ImageField(upload_to="students/",null=True,blank=True)
    dob = models.DateField()
    className = models.OneToOneField("Classes",on_delete=models.CASCADE)
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name