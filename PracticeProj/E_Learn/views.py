from django.shortcuts import render
from .models import User,Course, Enrollment, EnrollmentItem
from .serializers import UserSerializer,CourseSerializer, EnrollmentSerializer, EnrollmentItemSerializer
from rest_framework import generics

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all() 
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentItemListCreateView(generics.ListCreateAPIView): 
    queryset = EnrollmentItem.objects.all()
    serializer_class = EnrollmentItemSerializer

class EnrollmentItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):   
    queryset = EnrollmentItem.objects.all()
    serializer_class = EnrollmentItemSerializer

# Create your views here.
