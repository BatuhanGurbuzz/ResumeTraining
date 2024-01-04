from django.http import JsonResponse
from django.shortcuts import render
from contact.models import Message
def contact_form(request):
    if request.POST:
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
        
        success = True
        Requestmessage = 'Contact form sent successfully'
    else:
        success = False
        Requestmessage = 'Request method is not valid'
    context = {
        'success': success, 
        'message': Requestmessage,
    }
    
    return JsonResponse(context)

def contact(request):
    return render(request, 'contact.html')