from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

from .forms import ContactForm


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            template = get_template('contact_template.txt')

            Context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(Context)

            email = EmailMessage(
                'New contact form submission',
                content,
                'Your website <hi@wddinglovely.com>',
                ['youremail@gmail.com'],
                headers={'Reply-To': contact_email }
            )
            email.send()
            return redirect('/')

    template_name = 'contact.html'
    return render(request, template_name, context={
        'form': form_class,
    })