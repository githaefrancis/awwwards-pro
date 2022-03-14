from django.shortcuts import render,redirect
from .forms import ProjectForm
from .models import Project
# Create your views here.

def index(request):
  all_projects=Project.get_all_projects()
  context={
    "projects":all_projects,
  }
  return render(request,'index.html',context)

def new_project(request):
  if request.method=='POST':
    form=ProjectForm(request.POST,request.FILES)
    current_user=request.user

    if form.is_valid():
      new_project=form.save(commit=False)
      new_project.user=current_user
      new_project.save_project()

      return redirect('home')
  
  
  
  form=ProjectForm()
  context={
    "form":form,
  }
  return render(request,'new_project.html',context)