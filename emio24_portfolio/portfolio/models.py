from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name="Project Name")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    short_description = models.TextField(max_length=300, verbose_name="Short Description")
    full_description = models.TextField(verbose_name="Full Description")
    client_name = models.CharField(max_length=100, blank=True, null=True, 
                                 verbose_name="Client Name", 
                                 help_text="Leave blank for personal projects")
    repository_url = models.URLField(blank=True, null=True, verbose_name="Repository URL")
    completion_date = models.DateField(verbose_name="Completion Date")
    is_featured = models.BooleanField(default=False, verbose_name="Featured Project")
    display_order = models.PositiveIntegerField(default=0, verbose_name="Display Order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', '-completion_date']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/', verbose_name="Image")
    alt_text = models.CharField(max_length=200, verbose_name="Alternative Text")
    caption = models.CharField(max_length=200, blank=True, null=True, verbose_name="Caption")
    display_order = models.PositiveIntegerField(default=0, verbose_name="Display Order")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order']
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"Image for {self.project.name}"

class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Service Name")
    description = models.TextField(verbose_name="Service Description")
    icon_class = models.CharField(max_length=100, blank=True, null=True, 
                                verbose_name="Icon Class",
                                help_text="e.g., 'fas fa-laptop-code' for FontAwesome")
    display_order = models.PositiveIntegerField(default=0, verbose_name="Display Order")
    is_active = models.BooleanField(default=True, verbose_name="Active Service")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order']
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name

class Technology(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('database', 'Database'),
        ('design', 'Design Tool'),
        ('devops', 'DevOps'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Technology Name")
    logo = models.ImageField(upload_to='tech_logos/', blank=True, null=True, 
                           verbose_name="Logo/Icon")
    proficiency_level = models.CharField(max_length=50, blank=True, null=True,
                                       verbose_name="Proficiency Level",
                                       help_text="e.g., Expert, Advanced, Intermediate")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, 
                              default='other', verbose_name="Category")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
        ordering = ['category', 'name']

    def __str__(self):
        return self.name

class ProjectTechnology(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='technologies_used')
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    usage_context = models.CharField(max_length=200, blank=True, null=True,
                                   verbose_name="Usage Context",
                                   help_text="e.g., 'Used for backend API'")

    class Meta:
        verbose_name = "Project Technology"
        verbose_name_plural = "Project Technologies"
        unique_together = ('project', 'technology')

    def __str__(self):
        return f"{self.project.name} - {self.technology.name}"

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100, verbose_name="Client Name")
    client_company_or_role = models.CharField(max_length=200, blank=True, null=True,
                                            verbose_name="Company/Role")
    quote_text = models.TextField(verbose_name="Testimonial Quote")
    date_received = models.DateField(blank=True, null=True, verbose_name="Date Received")
    is_visible = models.BooleanField(default=True, verbose_name="Visible on Site")
    display_order = models.PositiveIntegerField(default=0, verbose_name="Display Order")
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True,
                              related_name='testimonials')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order']
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"Testimonial from {self.client_name}"

class ContactSubmission(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    phone_number = models.CharField(max_length=20, blank=True, null=True,
                                  verbose_name="Phone Number")
    subject = models.CharField(max_length=200, blank=True, null=True, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    submission_date = models.DateTimeField(auto_now_add=True, verbose_name="Submission Date")
    is_read = models.BooleanField(default=False, verbose_name="Mark as Read")

    class Meta:
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"
        ordering = ['-submission_date']

    def __str__(self):
        return f"Message from {self.full_name} on {self.submission_date}"

class SitePage(models.Model):
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL Slug")
    title = models.CharField(max_length=200, verbose_name="Page Title")
    content = models.TextField(verbose_name="Page Content")
    meta_description = models.CharField(max_length=300, blank=True, null=True,
                                      verbose_name="Meta Description")
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name="Last Modified")

    class Meta:
        verbose_name = "Site Page"
        verbose_name_plural = "Site Pages"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'slug': self.slug})
    
