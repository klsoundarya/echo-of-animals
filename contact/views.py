from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .models import Contact
from .forms import ContactForm

# contact views.py

def contact(request):
    form = ContactForm(request.POST or None)
    contacts = None
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "I aim to respond within 2 working days. Thank you for submitting the form!")
            return redirect('contact') 
            
    if request.user.is_superuser:
        contacts = Contact.objects.all().order_by('-created_at')

    return render(request, 'contact/contact.html', {'form': form, 'contacts': contacts})
