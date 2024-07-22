from django.shortcuts import render


def HomePage(request):
    return render(request, 'homepage.html')


def LoguinPage(request):
    return render(request, 'loguin.html')