# portfolio/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages # For displaying success/error messages
from .models import Project, Service, Testimonial, ContactMessage, Technology
from .forms import ContactForm # Import the form we just created

def home(request):
    """
    Renders the homepage with featured projects, services, and testimonials.
    """
    # Fetch featured projects (e.g., top 3)
    featured_projects = Project.objects.filter(is_featured=True).order_by('-completion_date')[:3]
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        'featured_projects': featured_projects,
        'services': services,
        'testimonials': testimonials,
    }
    return render(request, 'portfolio/home.html', context)

def project_list(request):
    """
    Renders the page listing all projects with pagination.
    """
    all_projects = Project.objects.all()
    paginator = Paginator(all_projects, 6) # Show 6 projects per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'portfolio/projects.html', context)

def project_detail(request, slug):
    """
    Renders the detailed view for a single project.
    """
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
    }
    return render(request, 'portfolio/project_detail.html', context)

def service_list(request):
    """
    Renders the page listing all services.
    """
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'portfolio/services.html', context)

def contact_view(request):
    """
    Handles the contact form submission and renders the contact page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # Saves the contact message to the database
            messages.success(request, 'Your message has been sent successfully! I will get back to you shortly.')
            return redirect('contact') # Redirect to prevent resubmission on refresh
        else:
            messages.error(request, 'There was an error with your submission. Please correct the errors below.')
    else:
        form = ContactForm() # Create an empty form for GET requests

    context = {
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)

