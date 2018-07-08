from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as authView
from accounts.views import userLogin, signup,register, dashboard
app_name = 'accounts'
urlpatterns = [
    path('login/', userLogin, name = 'login'),
    # path('login/', authView.LoginView.as_view(), name='logout'),
    path('logout/', authView.LogoutView.as_view(), name='logout'),
    path('signup/', register, name = 'signup'),
    path('dashboard/<username>/',dashboard, name= 'dashboard' )
]
