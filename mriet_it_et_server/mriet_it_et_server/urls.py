"""mriet_it_et_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from events.views import registerEvent,getroll
from events.views import dashboard,done_payment,getDetails,paid,unpaid,pending,export_to_excel,filter_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',getroll),
    path('register',registerEvent),
    # path('register/<str:roll>',registerEvent),
    path('accounts/login',LoginView.as_view(),name='login_url'),
    path('logout',LogoutView.as_view(),name='logout_url'),
    path('payment/paid/<str:roll>',done_payment),
    path('dashboard/detail/<str:roll>',getDetails),
    path('dashboard',dashboard),
    path('paid',paid),
    path('unpaid',unpaid),
    path('pending',pending),
    path('export',export_to_excel),
    path('filter',filter_data),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
