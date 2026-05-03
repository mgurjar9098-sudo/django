from django.shortcuts import render, HttpResponseRedirect

from .models import User
from .forms import StudentsRegisteration

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm=StudentsRegisteration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg =User(name=nm,email=em,password=pw)
            reg.save()
            fm=StudentsRegisteration()
            # fm.save()
    else: 
        fm=StudentsRegisteration()
    stud=User.objects.all()
    # print(stud)
    return render(request,'enroll/add_show.html',{'form':fm,'stu':stud}) 

    #this function for delete the data
def delete_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return  HttpResponseRedirect('/')

#this function will update /edit
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm=StudentsRegisteration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm=StudentsRegisteration(instance=pi)
    return render(request,'enroll/update_students.html',{'form':fm})