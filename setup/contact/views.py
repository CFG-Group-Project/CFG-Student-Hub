from django.shortcuts import render
from .models import ContactUs
from .forms import ContactForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

# Create your views here.
@login_required(login_url='/login/')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = ContactUs(user=request.user, subject=request.POST['subject'], content=request.POST['content'])
            contact.save()
            form = ContactForm()
        messages.success(request, "Your message has been sent!")
    else:
        form = ContactForm()
    notes = ContactUs.objects.filter(user=request.user).filter
    context = {'notes': notes, 'form': form }  # 'search': search
    return render(request, 'contact/contact.html', context)



