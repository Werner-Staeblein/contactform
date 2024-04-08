from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
        
            try:
                # Using the email entered by the user as the sender
                send_mail(
                    subject,
                    message,
                    email,  # Use the user's email as the sender
                    ['codeinstitutetest0@gmail.com']  # Your email as the recipient
                )

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('form_success')
    else:
        form = ContactForm()
    return render(request, 'send_email/contact_form.html', {'form': form})

def form_success_view(request):
    return HttpResponse('Vielen Dank für Ihre Nachricht!')
