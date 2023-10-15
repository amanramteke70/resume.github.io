from django.shortcuts import render
from django.shortcuts import redirect
from APP.models import Contact

# Create your views here.

def index(request):
    emp = Contact.objects.all()
    context = {
        'emp': emp,
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
    emp = Contact(
        fname = fname,
        phone = phone,
        email = email,
        message = message
    )
    emp.save()
    return redirect('home')
