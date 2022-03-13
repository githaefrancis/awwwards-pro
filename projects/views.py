from django.shortcuts import render,redirect
from .forms import ProjectForm
# Create your views here.

def index(request):
  return render(request,'index.html')

def new_project(request):
  if request.method=='POST':
    form=ProjectForm(request.POST,request.FILES)
    current_user=request.user

    if form.is_valid():
      new_project=form.save(commit=False)
      new_project.user=current_user
      new_project.save()

      return redirect('home')
  
  
  
  form=ProjectForm()
  context={
    "form":form,
  }
  return render(request,'new_project.html',context)