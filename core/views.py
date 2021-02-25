from django.shortcuts import render, HttpResponse

# Create your views here.              vista de los templates o de las plantillas de esta aplicacion (core)




def home(request):
    return render(request, "core/home.html")





def about(request):
    return render(request, "core/about.html")







def contact(request):
    return render(request, "core/contacto.html")