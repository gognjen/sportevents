from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Message

# Create your views here.
def home_page(request):    
    
    if request.method == 'POST':
        new_message = request.POST.get('message', '')
        Message.objects.create(text=new_message)
        return redirect('/invitations/test-sample/')   
        
    return render(request, 'home.html')
    

def view_invitation(request):
    messages = Message.objects.all()        
    return render(request, 'invitation.html', {'messages': messages})
