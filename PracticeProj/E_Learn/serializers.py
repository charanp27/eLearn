from .models import User, Course, Enrollment, EnrollmentItem
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    # email = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'role']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'price', 'instructor']

class EnrollmentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollmentItem
        fields = ['id', 'enrollment', 'progress', 'completion_status']

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    items = EnrollmentItemSerializer(many=True, read_only=True) 
    class Meta:
        model = Enrollment
        fields = '__all__'