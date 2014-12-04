from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Message, Invitation

# Create your views here.
def home_page(request):             
    return render(request, 'home.html')
    

def view_invitation(request, invitation_id):
    invitation = Invitation.objects.get(id=invitation_id)    
    return render(request, 'invitation.html', {'invitation': invitation})
    

def new_invitation(request):
    invitation = Invitation.objects.create()
    Message.objects.create(text=request.POST['message'], invitation=invitation)
    return redirect('/invitations/%d/' % (invitation.id,))


def add_message(request, invitation_id):
    invitation = Invitation.objects.get(id=invitation_id)
    Message.objects.create(text=request.POST['message'], invitation=invitation)
    return redirect('/invitations/%d/' % (invitation.id))
