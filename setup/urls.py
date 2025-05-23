"""
URL configuration for miaudota project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app_cadastro_usuario.views import LoginView
from app_home import views as home_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.landing_page, name='landing_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', include('app_home.urls')),
    path('agenda/', include('app_agendamento.urls')),
    path('estoque/', include('app_estoque.urls')),
    path('financas/', include('app_financas.urls')),
    path('usuarios/', include('app_cadastro_usuario.urls')),
    path('perfil/', include('app_perfil.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)