"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views
from blog import views as blog_views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from home import views as home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name="register"),
    path('profile/',user_views.profile,name="profile"),
    path('',include('blog.urls')),
    path('home/', login_required(home_view.home),name='home'),
    # path('',include('home.urls')),
    # django provides login and logout view(form) for us, but we still need to implement the html template
    # quote for customize loginView: https://www.youtube.com/watch?v=8V-mscw6H64
    path('login/',auth_views.LoginView.as_view(template_name ='user/login.html'),name="login"),
    path('logout/',user_views.logout_view,name="logout"),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name ='user/password_reset.html'),
        name="password_reset"),
    path('password-reset/done',
        auth_views.PasswordResetDoneView.as_view(template_name ='user/password_reset_done.html'),
        name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name ='user/password_reset_confirm.html'),
        name="password_reset_confirm"),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name ='user/password_reset_complete.html'),
        name="password_reset_complete")
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
