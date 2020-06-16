'''
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .models import WorkProfile, Activity, Education, Work, Project
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError




# Acitvity


        name = request.POST["name"]
        bioData = request.POST["bio"]
        workProfile = Profile(user=request.user, name=name, bio=bioData)
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
            workProfile = Profile.objects.get(user_id=request.user.id)
        except Profile.DoesNotExist:
            return render(request, "flights/workProCreate.html")
        context={
            "user": request.user,
            "profile": workProfile,
            "educations": workProfile.education.all(),
            "works": workProfile.work.all(),
            "projects": workProfile.projects.all(),
        }    
        return render(request, "flights/workPro.html", context)   



## Portfolio

# CREATORS 
def eduCreate(request):
    if request.method == 'GET':
        return render(request, "flights/portfolio/eduCreate.html")
    if request.method == 'POST':
        school = request.POST["school"]
        degree = request.POST["degree"]
        field = request.POST["field"]
        about = request.POST["about"]
        education = Education(school=school, degree=degree, field=field, about=about )
        education.save()
        eduId = education.id

        try:
            education = Education.objects.get(id=eduId)
        except Education.DoesNotExist:
            return render(request, "flights/portfolio/eduCreate.html")
        
        try:
            profile = Profile.objects.get(user_id=request.user.id)
            edu = profile.education
            edu.add(education)
        except Profile.DoesNotExist:
            return render(request, "flights/login.html")

        context={
        "education": education
        }
        return render(request, "flights/portfolio/eduDisplay.html", context)


def workCreate(request):
    if request.method == 'GET':
        return render(request, "flights/portfolio/workCreate.html")
    if request.method == 'POST':
        company = request.POST["company"]
        title = request.POST["title"]
        is_ongoing = request.POST.get('ongoing', 'False')
        about = request.POST["about"]
        if is_ongoing == 'on':
            ongoing = True
        else:
            ongoing = False

        work = Work(company=company, title=title, ongoing=ongoing, about=about )
        work.save()
        workId = work.id

        try:
            work = Work.objects.get(id=workId)
        except Work.DoesNotExist:
            return render(request, "flights/portfolio/workCreate.html")
        
        try:
            profile = Profile.objects.get(user_id=request.user.id)
            workProfile = profile.work
            workProfile.add(work)
        except Profile.DoesNotExist:
            return render(request, "flights/login.html")

        context={
        "work": work
        }
        return render(request, "flights/portfolio/workDisplay.html", context)


def projectCreate(request):
    if request.method == 'GET':
        return render(request, "flights/portfolio/projectCreate.html")
    if request.method == 'POST':
        shortAbout = request.POST["shortAbout"]
        title = request.POST["title"]
        longAbout = request.POST["longAbout"]
       
        project = Project(shortAbout=shortAbout, title=title, longAbout=longAbout)
        project.save()
        projectId = project.id

        try:
            project = Project.objects.get(id=projectId)
        except Project.DoesNotExist:
            return render(request, "flights/portfolio/projectCreate.html")
        
        try:
            profile = Profile.objects.get(user_id=request.user.id)
            profile.projects.add(project)
        except Profile.DoesNotExist:
            return render(request, "flights/login.html")

        context={
        "project": project
        }
        return render(request, "flights/portfolio/projectDisplay.html", context)    
    
# EDITORS 

def projectEdit(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
        profile = Profile.objects.get(id=request.user.id)
    except Project.DoesNotExist:
        return HttpResponseRedirect(reverse('projectCreate'))
    except Profile.DoesNotExist:
        return HttpResponseRedirect(reverse('myprofile'))


    if request.method == 'GET':
        context={
        "project": project}
        return render(request, "flights/portfolio/projectEdit.html", context)
    if request.method == 'POST':
        project.shortAbout = request.POST["shortAbout"]
        project.title = request.POST["title"]
        project.longAbout = request.POST["longAbout"]       
        project.save()
        
        context={
        "project": project
        }
        return render(request, "flights/portfolio/projectDisplay.html", context)    


def workEdit(request, work_id):
    try:
        work = Work.objects.get(id=work_id)
    except Work.DoesNotExist:
        return render(request, "flights/myprofile.html")

    if request.method == 'GET':
        context={
        "work": work}
        return render(request, "flights/portfolio/workEdit.html", context)
    if request.method == 'POST':
        work.company = request.POST["company"]
        work.title = request.POST["title"]
        is_ongoing = request.POST.get('ongoing', 'False')
        work.about = request.POST["about"]
        if is_ongoing == 'on':
            work.ongoing = True
        else:
            work.ongoing = False

        work.save()
        context={
        "work": work
        }
        return render(request, "flights/portfolio/workDisplay.html", context)            
    

def eduEdit(request, edu_id):
    try:
        education = Education.objects.get(id=edu_id)
    except Work.DoesNotExist:
        return render(request, "flights/portfolio/eduCreate.html")

    if request.method == 'GET':
        context={
        "education": education}
        return render(request, "flights/portfolio/eduEdit.html", context)
    if request.method == 'POST':
        education.school = request.POST["school"]
        education.degree = request.POST["degree"]
        education.field = request.POST["field"]
        education.about = request.POST["about"]
        education.save()
        
        context={
        "education": education
        }
        return render(request, "flights/portfolio/eduDisplay.html", context)
        





# PROFILES AND USER_USER INTERACTION.

def myportfolio(request):
    if request.method == 'GET':
        try:
            profile = Profile.objects.get(user_id=request.user.id)
        except Profile.DoesNotExist:
            return render(request, "flights/profileCreate.html", context)
        context={
            "username": request.user.username,
            "profile": profile,
            "projects": profile.projects.all(),
        }    
        return render(request, "flights/myportfolio.html", context)    


def profile(request, user_id):    
      if request.method == 'GET':      
        try:
            profile = Profile.objects.get(user_id=user_id)
            friends = profile.friends.all()
            requests = profile.friendRequests.all()
            user = User.objects.get(id=user_id)
        except Profile.DoesNotExist:    
            raise Http404("This user hasn't made a profile yet.")
        context={
            "user": user, 
            "profile": profile,
            "educations": profile.education.all(),
            "works": profile.work.all(),
        }
        return render(request, "flights/profileDisplay.html", context)  

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
        return render(request, "flights/workProfile.html", context)    

    
    if request.method == 'GET':
        try:
            workProfile = WorkProfile.objects.get(user_id=request.user.id)
        except WorkProfile.DoesNotExist:
            return render(request, "flights/workProCreate.html", context)
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
        username = request.POST["username"]
        password = request.POST["password"]
        
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
        


'''