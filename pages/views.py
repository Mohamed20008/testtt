from django.shortcuts import render
from .models import Login
from .forms import LoginForms
# from django.http import HttpResponse
 # Create your views here.
def index(request):
    LoginForms(request.POST).save()
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # data = Login(username = username, password= password)
    # data.save()
    return render(request, 'pages/index.html',{'form' : LoginForms})
