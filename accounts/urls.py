from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as authView
from accounts.views import userLogin, signup,register, dashboard
from django.conf import settings
from django.conf.urls.static import static
app_name = 'accounts'
urlpatterns = [
    path('login/', userLogin, name = 'login'),
    # path('login/', authView.LoginView.as_view(), name='logout'),
    path('logout/', authView.LogoutView.as_view(), name='logout'),
    path('signup/', register, name = 'signup'),
    path('dashboard/<username>/',dashboard, name= 'dashboard' )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
