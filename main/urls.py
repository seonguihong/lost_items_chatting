"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import signup_view, redirect_to_login  # signup_view와 redirect_to_login을 임포트

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('signup/', signup_view, name='signup'),
    path('chatbot/', include('chatbot.urls')),
    path('', RedirectView.as_view(url=reverse_lazy('login')), name='home'),
    path('redirect-to-login/', redirect_to_login, name='redirect_to_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
