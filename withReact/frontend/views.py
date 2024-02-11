from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def site_management(request):
    if not request.user.is_superuser:
        return redirect('403')
        
    return render(request, 'staff/index.html')


def Error_403(request):
    return render(request, 'errors/403.html')