import sys 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class NewVisitortest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url
              
    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()
                                    

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)        

    def tearDown(self):
        self.browser.quit()        
        
    def check_message_in_comments(self, message):
        comments_list = self.browser.find_element_by_id('id_ul_comments')
        comments = comments_list.find_elements_by_tag_name('li')
        self.assertIn(message, [comment.text for comment in comments])                        
        
    def test_can_write_an_invitation_and_retrieve_it_later(self):                
        # Zarko je cuo za novu web aplikaciju koja mu moze pomoci da organizuje 
        # svoje sportske aktivnosti. Otvara pocetnu stranicu da vidi o cemu se 
        # tu radi.
        self.browser.get(self.server_url)

        # Primjecuje da naslov stranice i zaglavlje spominju
        # sportskih aktivnosti.
        self.assertIn('sportske aktivnosti', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('sportske aktivnosti', header_text)
        
        # Pozvan je da napise pozivnicu za svoju prvu aktivnost
        inputbox = self.browser.find_element_by_id('id_new_message')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter an invitation message'
        )
        
        # Upisuju "Termin 10.01.! Hajmo prijave! :)" u text box 
        inputbox.send_keys('Termin 10.01.! Hajmo prijave! :)')

        # Kada pritisne enter, stranica se azurira i prikazuje se pozivnica
        # koju je upravo napisao "Termin 10.01.! Hajmo prijave! :)"
        inputbox.send_keys(Keys.ENTER)
        zarko_invitation_url = self.browser.current_url
        self.assertRegex(zarko_invitation_url, '/invitations/.+')
        self.check_message_in_comments('Termin 10.01.! Hajmo prijave! :)')

        # Tu se i dalje nalazi text box koji poziva da napise odgovor na pozivnicu
        # ili dodatni komentar. On upisuje "Zarko" da bi drugi znali da je on 
        # napisao pozivnicu.
        inputbox = self.browser.find_element_by_id('id_new_message')        
        inputbox.send_keys('Zarko')
        inputbox.send_keys(Keys.ENTER)                 

        # Stranica se ponovo osvježava i sada se ispod postojeće poruke vidi drugi
        # komentar.
        self.check_message_in_comments('Termin 10.01.! Hajmo prijave! :)')
        self.check_message_in_comments('Zarko')                

        # Sada novi korisnik, Ognjen, dolazi na stranicu
        
        ## Koristimo novu sesiju da bi bili sigurni  da ne 
        ## postoje nikakve informacije o Zarkovoj sesiji
        ## (cookies i tome slicno)
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        # Ognjen posjecuje pocetnu stranicu. Nema traga Zarkovoj pozivnici
        
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Termin 10.01.! Hajmo prijave! :)', page_text)
        self.assertNotIn('Zarko', page_text)
        
        # Ognjen pocinje pisati novu pozivnicu
        inputbox = self.browser.find_element_by_id('id_new_message')
        inputbox.send_keys('Hoce li neko fudbala u nedjelju?')
        inputbox.send_keys(Keys.ENTER)
        
        # Ognjen dobiva svoj vlastiti jedinstveni URL
        ognjen_invitation_url = self.browser.current_url
        self.assertRegex(ognjen_invitation_url, '/invitations/.+')
        self.assertNotEqual(ognjen_invitation_url, zarko_invitation_url)
        
        # Ponovo, nema traga Zarkovim porukama
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Termin 10.01.! Hajmo prijave! :)', page_text)
        self.assertIn('Hoce li neko fudbala u nedjelju?', page_text)

        # Zadovoljni, obojica odlaze na spavanje.

if __name__ == '__main__':
    unittest.main(warnings='ignore')


