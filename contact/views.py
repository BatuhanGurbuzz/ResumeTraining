from django.http import JsonResponse
from django.shortcuts import render
from contact.models import Message
from contact.forms import ContactForm
def contact_form(request):
    
    if request.POST:
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            name = request.POST.get('name')
            
            email = request.POST.get('email')
            
            subject = request.POST.get('subject')
            
            message = request.POST.get('message')
            
            Message.objects.create(
                name = name,
                email = email,
                subject = subject,
                message = message,
            )
            
            contact_form.send_mail()
            
            success = True
            Requestmessage = 'Contact form sent successfully'
        else:
            success = False
            Requestmessage = 'Contact form is not valid'
    else:
        success = False
        Requestmessage = 'Request method is not valid'
    context = {
        'success': success, 
        'message': Requestmessage,
    }
    
    return JsonResponse(context)

def contact(request):
    contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'contact.html', context)