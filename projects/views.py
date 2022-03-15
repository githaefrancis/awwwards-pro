from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .forms import ProjectForm
from .models import Project,Rating
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

def single_project(request,id):
  project=Project.objects.filter(pk=id).first()
  current_user=request.user
  has_rated=Rating.check_if_user_has_rated(current_user,id)
  average_ratings=Rating.get_average_rating(id)
  context={
    "project":project,
    "choices":[1,2,3,4,5,6,7,8,9,10],
    "has_rated":has_rated,
    "design_score":average_ratings['design'],
    "usability_score":average_ratings['usability'],
    "content_score":average_ratings['content']
  }
  
  
  return render(request,'project.html',context)


def vote(request,id):
  design_rating=request.POST.get('designoptions')
  usability_rating=request.POST.get("usabilityoptions")
  content_rating=request.POST.get("contentoptions")
  current_user=request.user
  target_project=Project.objects.filter(pk=id).first()

  new_rating=Rating(design_rating=design_rating,usability_rating=usability_rating,content_rating=content_rating,user=current_user,project=target_project)
  new_rating.save()
  data={'success':'You have been successfully rated this project'}
  return JsonResponse(data)
  

  
  # return render(request,'vote.html')
