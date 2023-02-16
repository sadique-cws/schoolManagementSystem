from django.contrib import admin
from django.urls import path
from schoolwork.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homepage,name="homepage"),
    path("apply/", applyForAdmission, name="apply"),
    path("accounts/login/", login, name="login"),
    path("accounts/logout/", logoutFunction, name="logout"),
    path("manage/student",manageStudents, name="manageStudent"),
    path("manage/admission/", manageAdmission, name="manageAdmission"),
    path("manage/student/<int:id>/delete/",deleteStudent, name="deleteStudent"),
    path("manage/student/<int:id>/edit/", editStudent, name="editStudent"),
    path("manage/student/<int:id>/view/", viewStudent, name="viewStudent"),
    path("manage/student/<int:id>/approve/", approve, name="approve"),
    path("manage/classes",manageClasses, name="manageClasses"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
