from django.shortcuts import render
from django.contrib.auth.models import User
from useaccounts.models import Student
import datetime
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        print('2' * 100)
        print(request.user.first_name, request.user.last_name, request.user.email, request.user.password,
              request.user.username)
        student = Student.objects.create(first_name=request.user.first_name, last_name=request.user.last_name,
                                         email=request.user.email,
                                         username=request.user.username, date=datetime.datetime.now())
        student.save()
        messages.success(request, 'Куттуктайбыз ийгиликтуу катталдыныз!!')
    return render(request, 'website/index.html')
# first_name = models.CharField(max_length=50)
#    last_name = models.CharField(max_length=50)
#    email = models.EmailField()
#    password = models.CharField(max_length=50)
#    username = models.CharField(max_length=250, null=True)
