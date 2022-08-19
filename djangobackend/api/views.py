from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
class StudentList(ListAPIView):
  queryset = Student.objects.all()
  print('line 9',queryset)
  serializer_class = StudentSerializer
  print('line 9',queryset)
  print('line 10',serializer_class)
