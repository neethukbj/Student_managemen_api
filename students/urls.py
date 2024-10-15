from django.urls import path,include
from students.models import *
from .views import *

urlpatterns=[
    path("students/",StudentlistView.as_view(),name="students"),
    path("student/<int:pk>/",StudentDetailView.as_view(),name="studentdetail"),
    path("Attendances/",AttendanceCreateView.as_view(),name="Attendances"),
    path("Attendance/<int:pk>/",AttedanceDetailsView.as_view(),name="Attendance"),




]