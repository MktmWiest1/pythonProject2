from django.urls import path
from . import views
from .forms import LoginForm

app_name = "users"
urlpatterns = [
    path("register/", views.Registration.as_view(), name="registration"),

]


