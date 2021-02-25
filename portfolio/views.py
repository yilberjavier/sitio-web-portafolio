from django.shortcuts import render
from .models import Project

# Create your views here.              vista de los templates o plantillas de esta aplicacion (portfolio)


def portfolio(request):

    projects = Project.objects.all()

    data = {
        "projects":projects
    }
    return render(request, "portfolio/portafolio.html", data) 
