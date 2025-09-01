from django.shortcuts import render

# Create your views here.
def guia_view(request):
    return render(request, 'guia.html')