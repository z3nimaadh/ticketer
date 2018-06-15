from django.shortcuts import render
from .forms import SendData
from django.shortcuts import redirect
from userdata.models import Subdomain

# Create your views here.

def submit_page(request):
    return render(request, 'userdata/submit_page.html', {})

def alreadyexists(request):
    return render(request, 'userdata/alreadyexists.html', {})

def success(request):
    return render(request, 'userdata/success.html', {})

def send_data(request):
    if request.method == "POST":
        form = SendData(request.POST)
        if form.is_valid():
            
            if Subdomain.objects.filter(subdomain=form['subdomain'].value()).exists():
                print("already exists")
                return redirect('alreadyexists')
            else:
                data = form.save(commit=False)
                data.save()
                return redirect('success')


    else:
        form = SendData()
    return render(request, 'userdata/submit.html', {'form':form})