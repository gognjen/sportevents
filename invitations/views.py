from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Message

# Create your views here.
def home_page(request):             
    return render(request, 'home.html')
    

def view_invitation(request):
    messages = Message.objects.all()        
    return render(request, 'invitation.html', {'messages': messages})
    
def new_invitation(request):
    Message.objects.create(text=request.POST['message'])
    return redirect('/invitations/test-sample/')   
