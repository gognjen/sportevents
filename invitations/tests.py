from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from invitations.views import home_page
from django.template.loader import render_to_string
from invitations.models import Message

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
        
    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['message'] = 'A new comment' 
        
        response = home_page(request)
        
        self.assertEqual(Message.objects.count(), 1)
        new_message = Message.objects.first()
        self.assertEqual(new_message.text, 'A new comment')
        
    def test_home_page_redirects_after_POST(self):        
        request = HttpRequest()
        request.method = 'POST'
        request.POST['message'] = 'A new comment' 

        response = home_page(request)
            
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/invitations/test-sample/')        

    def test_saving_and_retreiving_messages(self):
        first_message = Message()
        first_message.text = 'The first (ever) message'
        first_message.save()
        
        second_message = Message()
        second_message.text = 'Message the second'
        second_message.save()
        
        saved_messages = Message.objects.all()
        self.assertEqual(saved_messages.count(), 2)
        
        first_saved_message = saved_messages[0]
        second_saved_message = saved_messages[1]
        
        self.assertEqual(first_saved_message.text, 'The first (ever) message')
        self.assertEqual(second_saved_message.text, 'Message the second')
    
    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Message.objects.count(), 0)    
        
    
class ListViewTest(TestCase):

    def test_uses_invitation_template(self):
        response = self.client.get('/invitations/test-sample/')
        self.assertTemplateUsed(response, 'invitation.html')
        
    
    def test_display_all_messages(self):
        Message.objects.create(text='message 1')
        Message.objects.create(text='message 2')
        
        response = self.client.get('/invitations/test-sample/')
        
        self.assertContains(response, 'message 1')
        self.assertContains(response, 'message 2')
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
