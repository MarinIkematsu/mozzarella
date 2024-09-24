from django.urls import path
from .views import HomeView
from django.contrib.auth.decorators import login_required


app_name = 'app'

urlpatterns = [
    path('home/', login_required(HomeView.as_view()), name='home')
]