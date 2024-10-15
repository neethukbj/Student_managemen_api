from rest_framework import serializers
from .serializers import StudentSerializer,AttendanceSerializer
from students.models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class StudentlistView(generics.ListCreateAPIView):
	queryset=Student.objects.all()
	serializer_class= StudentSerializer
	permission_class=[IsAuthenticated]
	

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset=Attendance.objects.all()
	serializer_class=StudentSerializer
	permission_class=[IsAuthenticated]


class AttendanceCreateView(generics.ListCreateAPIView):
	queryset=Attendance.objects.all()
	serializer_class=AttendanceSerializer
	permission_class=[IsAuthenticated]

class AttedanceDetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset=Attendance.objects.all()
	serializer_class=AttendanceSerializer
	permission_class=[IsAuthenticated]