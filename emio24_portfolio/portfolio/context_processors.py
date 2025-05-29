from .models import Service

def global_context(request):
    services = Service.objects.filter(is_active=True).order_by('display_order')[:5]
    return {
        'global_services': services,
    }