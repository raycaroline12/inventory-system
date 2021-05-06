from django.shortcuts import render

def inventory(request):
    return render(request, 'tables.html')
