# portfolio/urls.py

from django.urls import path
from . import views # Import views from the current directory

urlpatterns = [
    path('', views.home, name='home'), # Homepage
    path('projects/', views.project_list, name='projects'), # All projects list
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'), # Individual project detail
    path('services/', views.service_list, name='services'), # Services page
    path('contact/', views.contact_view, name='contact'), # Contact page
]