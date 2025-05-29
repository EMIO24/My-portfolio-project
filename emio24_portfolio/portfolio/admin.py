from django.contrib import admin
from .models import (
    Project, ProjectImage, Service, Technology, 
    ProjectTechnology, Testimonial, ContactSubmission, SitePage
)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'alt_text', 'caption', 'display_order')
    ordering = ('display_order',)

class ProjectTechnologyInline(admin.TabularInline):
    model = ProjectTechnology
    extra = 1
    autocomplete_fields = ['technology']

class TestimonialInline(admin.TabularInline):
    model = Testimonial
    extra = 0
    fields = ('client_name', 'client_company_or_role', 'quote_text', 'is_visible', 'display_order')
    ordering = ('display_order',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_name', 'completion_date', 'is_featured', 'display_order')
    list_filter = ('is_featured', 'completion_date')
    search_fields = ('name', 'client_name', 'short_description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProjectImageInline, ProjectTechnologyInline, TestimonialInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'is_featured', 'display_order')
        }),
        ('Description', {
            'fields': ('short_description', 'full_description')
        }),
        ('Details', {
            'fields': ('client_name', 'repository_url', 'completion_date')
        }),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'display_order')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    fields = ('name', 'description', 'icon_class', 'is_active', 'display_order')

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency_level')
    list_filter = ('category',)
    search_fields = ('name',)
    fields = ('name', 'logo', 'proficiency_level', 'category')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_company_or_role', 'is_visible', 'display_order', 'project')
    list_filter = ('is_visible', 'project')
    search_fields = ('client_name', 'quote_text')
    fields = ('client_name', 'client_company_or_role', 'quote_text', 'date_received', 
              'is_visible', 'display_order', 'project')

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'submission_date', 'is_read')
    list_filter = ('is_read', 'submission_date')
    search_fields = ('full_name', 'email', 'message')
    readonly_fields = ('submission_date',)
    fields = ('full_name', 'email', 'phone_number', 'subject', 'message', 
              'submission_date', 'is_read')

@admin.register(SitePage)
class SitePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'last_modified_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'content', 'meta_description')

admin.site.register(ProjectImage)
admin.site.register(ProjectTechnology)