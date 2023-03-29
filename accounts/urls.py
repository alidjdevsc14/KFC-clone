from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('usersignup/', views.usersignup, name='usersignup'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('userlogout/', views.user_logout_view, name='userlogout'),

]
