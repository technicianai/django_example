from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import (
    Student,
    Course,
    Enrollment
)
from .serializers import (
    StudentSerializer,
    CourseSerializer,
    EnrollmentSerializer
)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CreateEnrollmentView(CreateAPIView):
    def post(self, request):
        if not(request.data.get('student') and request.data.get('course')):
            return Response('student and course are required')
        
        try:
            enrollment = Enrollment.objects.get(
                student_id=request.data.get('student'),
                course_id=request.data.get('course')
            )
            return Response('student is already enrolled in course')
        except Enrollment.DoesNotExist:
            pass

        serializer = EnrollmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)