from django.shortcuts import render


def handle_404(request):
    return render(request, 'main/404.html')
