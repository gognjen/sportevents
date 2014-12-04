from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Message, Invitation

# Create your views here.
def home_page(request):             
    return render(request, 'home.html')
    

def view_invitation(request):
    messages = Message.objects.all()        
    return render(request, 'invitation.html', {'messages': messages})
    
def new_invitation(request):
    invitation = Invitation.objects.create()
    Message.objects.create(text=request.POST['message'], invitation=invitation)
    return redirect('/invitations/test-sample/')   
