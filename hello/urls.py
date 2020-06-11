from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("profile", views.myprofile, name="myprofile"),
    path("portfolio", views.myportfolio, name="myportfolio"),
    path("<int:user_id>/profile", views.profile, name="profile"),   
    path("activityCreate", views.activityCreate, name="activityCreate"),
    path("activities/<int:activity_id>", views.activityDisplay, name="activityDisplay"),
    path("eduCreate", views.eduCreate, name="eduCreate"),
    path("workCreate", views.workCreate, name="workCreate"),
    path("new-project", views.projectCreate, name="projectCreate"),
    path("projectEditor/<int:project_id>", views.projectEdit, name="projectEdit"),
    path("workEditor/<int:work_id>", views.workEdit, name="workEdit"),
    path("eduEditor/<int:edu_id>", views.eduEdit, name="eduEdit"),




]
