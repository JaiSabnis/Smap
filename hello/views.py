from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .models import Profile, Category, Education, Work, Post
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError


def profile(request):        
    if request.method == 'POST':
        if 'postSubmit' in request.POST:
            shortAbout = request.POST["shortAbout"]
            title = request.POST["title"]
            longAbout = request.POST["longAbout"]
            post = Post(shortAbout=shortAbout, title=title, longAbout=longAbout)
            post.save()
            try:
                profile = Profile.objects.get(user_id=request.user.id)
                profile.posts.add(post)
            except Profile.DoesNotExist:
                profile = Profile(user=request.user)
                profile.save()  
                profile.posts.add(post)
            context={
            "user": request.user,
            "profile": profile,
            "posts": profile.posts.all(),  
            "categorys": profile.categorys.all()}
            return render(request, "flights/webspace.html", context) 

        if 'catSubmit' in request.POST:
            about = request.POST["catAbout"]
            title = request.POST["catTitle"]
            cat = Category(about=about, title=title)
            cat.save()
            try:
                profile = Profile.objects.get(user_id=request.user.id)
                profile.categorys.add(cat)
            except Profile.DoesNotExist:
                profile = Profile(user=request.user)
                profile.save()  
                profile.categorys.add(cat)
            context={
            "user": request.user,
            "profile": profile,
            "posts": profile.posts.all(),
            "categorys": profile.categorys.all()}
            return render(request, "flights/webspace.html", context) 

        if 'catPost' in request.POST:
            catId = request.POST["category"]
            shortAbout = request.POST["postShortAbout"]
            title = request.POST["postTitle"]
            longAbout = request.POST["postLongAbout"]
            post = Post(shortAbout=shortAbout, title=title, longAbout=longAbout)
            post.save()

            profile = Profile.objects.get(user_id=request.user.id)
            category = profile.categorys.get(id=catId)
            category.posts.add(post)
            category.title = post.title
            category.save()
           
            context={
            "user": request.user,
            "profile": profile,
            "posts": profile.posts.all(),  
            "categorys": profile.categorys.all()}
            return render(request, "flights/webspace.html", context)


    if request.method == 'GET':
        try:
            profile = Profile.objects.get(user_id=request.user.id)
        except Profile.DoesNotExist:
            profile = Profile(user=request.user)
            profile.save()        
        context={
            "user": request.user,
            "profile": profile,
            "posts": profile.posts.all(),
            "categorys": profile.categorys.all()
            }
        return render(request, "flights/webspace.html", context)   



def postCreate(request):
    if request.method == 'GET':
        return render(request, "flights/postCreate.html")


    

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
        

