from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    # path('login/', views.login_user, name="login"),
    # path('logout/', views.log_out, name="logout"),
]