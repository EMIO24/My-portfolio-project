# Generated by Django 5.1.6 on 2025-05-29 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('subject', models.CharField(blank=True, max_length=200, null=True, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('submission_date', models.DateTimeField(auto_now_add=True, verbose_name='Submission Date')),
                ('is_read', models.BooleanField(default=False, verbose_name='Mark as Read')),
            ],
            options={
                'verbose_name': 'Contact Submission',
                'verbose_name_plural': 'Contact Submissions',
                'ordering': ['-submission_date'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Project Name')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('short_description', models.TextField(max_length=300, verbose_name='Short Description')),
                ('full_description', models.TextField(verbose_name='Full Description')),
                ('client_name', models.CharField(blank=True, help_text='Leave blank for personal projects', max_length=100, null=True, verbose_name='Client Name')),
                ('repository_url', models.URLField(blank=True, null=True, verbose_name='Repository URL')),
                ('completion_date', models.DateField(verbose_name='Completion Date')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Featured Project')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name='Display Order')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['display_order', '-completion_date'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Service Name')),
                ('description', models.TextField(verbose_name='Service Description')),
                ('icon_class', models.CharField(blank=True, help_text="e.g., 'fas fa-laptop-code' for FontAwesome", max_length=100, null=True, verbose_name='Icon Class')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name='Display Order')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active Service')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='SitePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL Slug')),
                ('title', models.CharField(max_length=200, verbose_name='Page Title')),
                ('content', models.TextField(verbose_name='Page Content')),
                ('meta_description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Meta Description')),
                ('last_modified_date', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name': 'Site Page',
                'verbose_name_plural': 'Site Pages',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Technology Name')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='tech_logos/', verbose_name='Logo/Icon')),
                ('proficiency_level', models.CharField(blank=True, help_text='e.g., Expert, Advanced, Intermediate', max_length=50, null=True, verbose_name='Proficiency Level')),
                ('category', models.CharField(choices=[('backend', 'Backend'), ('frontend', 'Frontend'), ('database', 'Database'), ('design', 'Design Tool'), ('devops', 'DevOps'), ('other', 'Other')], default='other', max_length=50, verbose_name='Category')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Technology',
                'verbose_name_plural': 'Technologies',
                'ordering': ['category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/', verbose_name='Image')),
                ('alt_text', models.CharField(max_length=200, verbose_name='Alternative Text')),
                ('caption', models.CharField(blank=True, max_length=200, null=True, verbose_name='Caption')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name='Display Order')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='portfolio.project')),
            ],
            options={
                'verbose_name': 'Project Image',
                'verbose_name_plural': 'Project Images',
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100, verbose_name='Client Name')),
                ('client_company_or_role', models.CharField(blank=True, max_length=200, null=True, verbose_name='Company/Role')),
                ('quote_text', models.TextField(verbose_name='Testimonial Quote')),
                ('date_received', models.DateField(blank=True, null=True, verbose_name='Date Received')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Visible on Site')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name='Display Order')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='testimonials', to='portfolio.project')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
                'ordering': ['display_order'],
            },
        ),
        migrations.CreateModel(
            name='ProjectTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage_context', models.CharField(blank=True, help_text="e.g., 'Used for backend API'", max_length=200, null=True, verbose_name='Usage Context')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technologies_used', to='portfolio.project')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.technology')),
            ],
            options={
                'verbose_name': 'Project Technology',
                'verbose_name_plural': 'Project Technologies',
                'unique_together': {('project', 'technology')},
            },
        ),
    ]
