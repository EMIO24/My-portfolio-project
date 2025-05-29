from django.urls import path
from .views import (
    HomeView, ProjectListView, ProjectDetailView, 
    ServiceListView, PageDetailView, ContactView,
    contact_success, technology_projects
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('services/', ServiceListView.as_view(), name='services'),
    path('page/<slug:slug>/', PageDetailView.as_view(), name='page_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
    path('technology/<int:tech_id>/', technology_projects, name='technology_projects'),
]