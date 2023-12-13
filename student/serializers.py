from rest_framework import serializers

from .models import (
    Student,
    Course,
    Enrollment
)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Student

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Course

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Enrollment
