from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .models import WorkProfile, Activity, Education, Work, Project
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError




def workPro(request):        
    if request.method == 'POST':
        name = request.POST["name"]
        bioData = request.POST["bio"]
        workProfile = WorkProfile(user=request.user, name=name, bio=bioData)
        workProfile.save()

        schools = request.POST.getlist('school')
        degrees = request.POST.getlist('degree')
        fields = request.POST.getlist('field')
        eduAbouts = request.POST.getlist('eduAbout')

        for i in range(len(schools)):
            edu = Education(school=schools[i], degree=degrees[i], field=fields[i], about=eduAbouts[i])
            edu.save()
            workProfile.education.add(edu)

        companys = request.POST.getlist('company')
        jobTitles = request.POST.getlist('job')
        workAbouts = request.POST.getlist('workAbout')

        for i in range(len(companys)):
            work = Work(company=companys[i], title=jobTitles[i], about=workAbouts[i])
            work.save()
            workProfile.work.add(work)

        projectTitles = request.POST.getlist('projectTitle')
        shortAbouts = request.POST.getlist('shortAbout')
        longAbouts = request.POST.getlist('longAbout')

        for i in range(len(projectTitles)):
            project = Project(title=projectTitles[i], shortAbout=shortAbouts[i], longAbout=longAbouts[i])
            project.save()
            workProfile.projects.add(project)

        context={
            "user": request.user,
            "profile": workProfile,
            "educations": workProfile.education.all(),
            "works": workProfile.work.all(),
        }    
        return render(request, "flights/workPro.html", context)    

    
    if request.method == 'GET':
        try:
            workProfile = WorkProfile.objects.get(user_id=request.user.id)
        except WorkProfile.DoesNotExist:
            return render(request, "flights/workProCreate.html")
        context={
            "user": request.user,
            "profile": workProfile,
            "educations": workProfile.education.all(),
            "works": workProfile.work.all(),
            "projects": workProfile.projects.all(),
        }    
        return render(request, "flights/workPro.html", context)    

    

# Auth

def register_view(request):
    if request.method == 'GET':
        return render(request, "flights/register.html", {"message":None})
    
    if request.method == 'POST': 
        try:
            user = User.objects.create_user(
                username = request.POST["username"],
                email = request.POST["email"],
                password = request.POST["password"])
            user.save()
        except IntegrityError:
            return render(request, "flights/register.html", {"message": "Username already exists"})
        
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "flights/register.html", {"message": "invalid credentials"})


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "flights/login.html", {"message": "invalid credentials"})

def logout_view(request):
    logout(request)
    return render(request, "flights/logout.html", {"message": "Logged out"})

def index(request):
    if not request.user.is_authenticated:
        return render(request, "flights/login.html", {"message": None})
    context = {
        "users": None,
    }
    return render(request, "flights/index.html", context)
        

