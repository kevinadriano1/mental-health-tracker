from django.shortcuts import render



# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306172552',
        'name': 'Kevin Adriano',
        'class': 'KKI'
    }

    return render(request, "main.html", context)
