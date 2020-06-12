from django.db import models
from django.contrib.auth.models import User


class Education(models.Model):
    school = models.CharField(max_length=100, blank=False)
    degree = models.CharField(max_length=100, blank=False)
    field = models.CharField(max_length=100, blank=True)
    about = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return f"{self.school}"

class Project(models.Model):
    title = models.CharField(max_length=100, blank=False)
    shortAbout = models.CharField(max_length=200, blank=False)
    longAbout = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return f"{self.title}"


class Skill(models.Model):
    name = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return f"{self.name}"

class Work(models.Model):
    company = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)
    ongoing = models.BooleanField(blank=True)
    about = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return f"{self.company}"

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   first = models.CharField(max_length=20, blank=True)
   last = models.CharField(max_length=20, blank=True)
   bio = models.CharField(blank=True, max_length=2000)
   birthdate = models.DateField(blank=True)
   education = models.ManyToManyField(Education, related_name="education", blank=True)
   skills = models.ManyToManyField(Skill, related_name="skills", blank=True)
   work = models.ManyToManyField(Work, related_name="work", blank=True)
   projects = models.ManyToManyField(Project, related_name="projects", blank=True)
   friendRequests = models.ManyToManyField(User, related_name="friendRequests", blank=True)
   friends = models.ManyToManyField(User, related_name="friends", blank=True)
#  displayPic = models.ImageField(upload_to='displayPics', blank=True)
   def __str__(self):
       return f"{self.first} {self.last}"

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=25, blank=False)
    caption = models.CharField(max_length=2000, blank=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}" 





