from django.shortcuts import render
from .models import Project , First
# Create your views here.
def index(request):
    Pro = Project.objects.all()
    First_page = First.objects.all()
    return render(request,'in/index.html',{'project':Pro,'first':First_page})