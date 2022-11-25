from django.urls import path
from . import views

app_name="reserve"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
 
    # API routs
    path("reserve",views.reserve, name="reserve"),
    path("mynobat",views.my_appointment,name="mynobat"),
    path("schedule",views.schedule,name="schedule"),
    path("getschedule",views.get_schedule,name="get_schedule"),
    path("initialstate",views.initialstate,name="initialstate"),


]