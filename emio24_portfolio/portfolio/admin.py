# portfolio/admin.py

from django.contrib import admin
from .models import (
    Technology, Project, ProjectImage, ProjectTechnology,
    Service, Testimonial, ContactMessage
)

# Inline for Project Images and Technologies
class ProjectImageInline(admin.TabularInline):
    """
    Allows adding/editing project images directly from the Project admin page.
    """
    model = ProjectImage
    extra = 1 # Number of empty forms to display

class ProjectTechnologyInline(admin.TabularInline):
    """
    Allows adding/editing project technologies directly from the Project admin page.
    """
    model = ProjectTechnology
    extra = 1

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo_preview')
    search_fields = ('name',)

    def logo_preview(self, obj):
        if obj.logo:
            from django.utils.html import format_html
            return format_html(f'<img src="{obj.logo.url}" style="max-height: 50px; width: auto;" />')
        return "No Image"
    logo_preview.short_description = "Logo"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_name', 'completion_date', 'is_featured', 'repository_url', 'live_url')
    list_filter = ('is_featured', 'completion_date')
    search_fields = ('name', 'short_description', 'full_description', 'client_name')
    prepopulated_fields = {'slug': ('name',)} # Automatically generate slug from name
    inlines = [ProjectImageInline, ProjectTechnologyInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'short_description', 'full_description', 'is_featured')
        }),
        ('Details', {
            'fields': ('client_name', 'completion_date', 'repository_url', 'live_url'),
            'classes': ('collapse',) # Makes this section collapsible in admin
        }),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class', 'description_snippet')
    search_fields = ('name', 'description')

    def description_snippet(self, obj):
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
    description_snippet.short_description = "Description Snippet"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_company_or_role', 'project', 'date_created')
    list_filter = ('project', 'date_created')
    search_fields = ('client_name', 'quote_text')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'subject', 'date_submitted', 'is_read')
    list_filter = ('is_read', 'date_submitted')
    search_fields = ('full_name', 'email', 'subject', 'message')
    list_editable = ('is_read',) # Allow changing 'is_read' directly from list view
    readonly_fields = ('full_name', 'email', 'phone_number', 'subject', 'message', 'date_submitted') # Prevent editing submitted messages
