from django.shortcuts import render
from .models import Task
from .forms import Task


# Create your views here.
def base(request):
    tasks = Task.objects.all()
    return render(request, 'html/base.html', {'tasks': tasks})


def Buy(request):
    tasks = Task.objects.all()
    # if request.method == 'POST':
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = TaskForm()
    return render(request, 'html/page2.html',{'title':'Главная страница сайта','tasks': tasks})


def Sell(request):
    # tasks = Task.objects.all()
    return render(request, 'html/page3.html', {'title': 'Создать продажу', })
