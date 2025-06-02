# portfolio/models.py

from django.db import models
from django.utils.text import slugify
from django.core.validators import RegexValidator

class Technology(models.Model):
    """
    Represents a technology used in projects (e.g., Python, React, Django).
    """
    name = models.CharField(max_length=100, unique=True)
    # Optional: URL to a logo for the technology
    logo = models.ImageField(upload_to='technology_logos/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['name']

    def __str__(self):
        return self.name

class Project(models.Model):
    """
    Represents a portfolio project.
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    short_description = models.CharField(max_length=255)
    full_description = models.TextField()
    client_name = models.CharField(max_length=100, blank=True, null=True)
    completion_date = models.DateField()
    repository_url = models.URLField(blank=True, null=True, verbose_name="GitHub/Repo URL")
    live_url = models.URLField(blank=True, null=True, verbose_name="Live Demo URL")
    is_featured = models.BooleanField(default=False, help_text="Check to display on the homepage.")

    class Meta:
        ordering = ['-completion_date'] # Order by most recent projects first

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate slug from the project name if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProjectImage(models.Model):
    """
    Images associated with a project.
    """
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    alt_text = models.CharField(max_length=255, blank=True, help_text="Descriptive text for accessibility.")
    caption = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Order in which images appear.")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image for {self.project.name} ({self.order})"

class ProjectTechnology(models.Model):
    """
    Intermediate model to link Projects and Technologies, allowing for usage context.
    """
    project = models.ForeignKey(Project, related_name='technologies_used', on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    usage_context = models.CharField(max_length=255, blank=True, help_text="How this technology was used in the project (e.g., 'Frontend UI', 'Backend API').")

    class Meta:
        unique_together = ('project', 'technology') # A technology can only be linked once per project
        verbose_name_plural = "Project Technologies"

    def __str__(self):
        return f"{self.technology.name} in {self.project.name}"

class Service(models.Model):
    """
    Represents a service offered (e.g., Web Development, Mobile App Development).
    """
    name = models.CharField(max_length=150)
    description = models.TextField()
    # Font Awesome icon class (e.g., 'fas fa-laptop-code')
    icon_class = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class (e.g., 'fas fa-laptop-code')")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    """
    Client testimonials.
    """
    client_name = models.CharField(max_length=100)
    client_company_or_role = models.CharField(max_length=150, blank=True, null=True)
    quote_text = models.TextField()
    # Link testimonial to a specific project (optional)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True, related_name='testimonials')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"Testimonial by {self.client_name}"

class ContactMessage(models.Model):
    """
    Stores messages submitted through the contact form.
    """
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    # Basic phone number validation (optional)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_submitted']

    def __str__(self):
        return f"Message from {self.full_name} ({self.email})"
