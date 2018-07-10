from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as authView
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static
app_name = 'accounts'
urlpatterns = [
    path('login/', userLogin, name = 'login'),
    # path('login/', authView.LoginView.as_view(), name='logout'),
    path('logout/', authView.LogoutView.as_view(), name='logout'),
    path('signup/', register, name = 'signup'),
    path('dashboard/<username>/',dashboard, name= 'dashboard' ),
    path('submit/', postPublish, name = 'publish-post'),
    path('friendship/',friendship,name='friendship'),
    path('break/', breakfriendship, name='break'),
    path('profile/<username>/<you>', getProfile, name='profile'),
    path('edit/<username>/', editProfile, name='editing'),
    path('setting/<username>/', profileSetting, name='setting'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
