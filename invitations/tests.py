from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from invitations.views import home_page
from django.template.loader import render_to_string
from invitations.models import Message, Invitation

# Create your tests here.
class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string(
            'home.html',
            {'message': 'A new message'}
        )
        self.assertEqual(response.content.decode(), expected_html)
        

class InvitationAndMessageModelTest(TestCase):

    def test_saving_and_retreiving_messages(self):
        invitation = Invitation()
        invitation.save()
    
        first_message = Message()
        first_message.text = 'The first (ever) message'
        first_message.invitation = invitation
        first_message.save()
        
        second_message = Message()
        second_message.text = 'Message the second'
        second_message.invitation = invitation
        second_message.save()
        
        saved_invitation = Invitation.objects.first()
        self.assertEqual(saved_invitation, invitation)
        
        saved_messages = Message.objects.all()
        self.assertEqual(saved_messages.count(), 2)
        
        first_saved_message = saved_messages[0]
        second_saved_message = saved_messages[1]
        
        self.assertEqual(first_saved_message.text, 'The first (ever) message')
        self.assertEqual(first_saved_message.invitation, invitation)
        self.assertEqual(second_saved_message.text, 'Message the second')   
        self.assertEqual(second_saved_message.invitation, invitation)
        
    
class InvitationViewTest(TestCase):

    def test_uses_invitation_template(self):
        response = self.client.get('/invitations/test-sample/')
        self.assertTemplateUsed(response, 'invitation.html')
        
    
    def test_display_all_messages(self):
        invitation = Invitation.objects.create()
        Message.objects.create(text='message 1', invitation=invitation)
        Message.objects.create(text='message 2', invitation=invitation)
        
        response = self.client.get('/invitations/test-sample/')
        
        self.assertContains(response, 'message 1')
        self.assertContains(response, 'message 2')
        
        
    def test_saveing_a_POST_request(self):
        self.client.post(
            '/invitations/new',
            data={'message': 'A new comment'}
        )
        
        self.assertEqual(Message.objects.count(), 1)
        new_message = Message.objects.first()
        self.assertEqual(new_message.text, 'A new comment')
        
    def test_redirects_after_POST(self):        
        response = self.client.post(
            '/invitations/new',
            data={'message': 'A new comment'}
        )           
        
        self.assertRedirects(response, '/invitations/test-sample/')                
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
