from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Project, Service, Technology, Testimonial, SitePage, ContactSubmission
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'portfolio/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_projects'] = Project.objects.filter(is_featured=True).order_by('display_order')[:3]
        context['services'] = Service.objects.filter(is_active=True).order_by('display_order')
        context['testimonials'] = Testimonial.objects.filter(is_visible=True).order_by('display_order')[:3]
        return context

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    paginate_by = 6
    
    def get_queryset(self):
        return Project.objects.all().order_by('display_order', '-completion_date')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        context['technologies'] = project.technologies_used.select_related('technology')
        return context

class ServiceListView(ListView):
    model = Service
    template_name = 'portfolio/services.html'
    context_object_name = 'services'
    
    def get_queryset(self):
        return Service.objects.filter(is_active=True).order_by('display_order')

class PageDetailView(DetailView):
    model = SitePage
    template_name = 'portfolio/page_detail.html'
    context_object_name = 'page'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class ContactView(CreateView):
    model = ContactSubmission
    form_class = ContactForm
    template_name = 'portfolio/contact.html'
    success_url = reverse_lazy('contact_success')
    
    def form_valid(self, form):
        # You could add email notification logic here
        return super().form_valid(form)

def contact_success(request):
    return render(request, 'portfolio/contact_success.html')

def technology_projects(request, tech_id):
    technology = get_object_or_404(Technology, pk=tech_id)
    projects = Project.objects.filter(technologies_used__technology=technology).order_by('display_order')
    context = {
        'technology': technology,
        'projects': projects
    }
    return render(request, 'portfolio/technology_projects.html', context)