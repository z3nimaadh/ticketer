from django.shortcuts import render

# Create your views here.

def submit_page(request):
    return render(request, 'userdata/submit_page.html', {})