from django.shortcuts import render
from django.http import Http404
from .models import Services, Subservices


def services(request):
    all_services = Services.objects.all()
    return render(request, 'dashboard/index.html', {'all_services': all_services})


def subservices(request, service_chosen):
    try:
        service_chosen = str(service_chosen)
        service = Services.objects.get(service_name = service_chosen)
        subservices = Subservices.objects.filter(service_name__service_name = service.service_name)
        subservices = [subs for subs in subservices]
    except Services.DoesNotExist:
        raise Http404("Service does not exist: "+service_chosen)
    return render(request, 'dashboard/service.html/', {'subservices':subservices, 'service_name': service.service_name})

def service_function(request, service_chosen, subservice_chosen):
    try:
        service_chosen = str(service_chosen)
        subservice_chosen = str(subservice_chosen)
        service = Services.objects.get(service_name=service_chosen)
        subservice = Subservices.objects.get(subservice_name = subservice_chosen)

    except Services.DoesNotExist:
        raise Http404("Service does not exist: " + service_chosen)
    except Subservices.DoesNotExist:
        raise Http404("Subservice requested does not exist: " + subservice_chosen)
    return render(request, 'dashboard/subservice.html', {'subservice': subservice})


