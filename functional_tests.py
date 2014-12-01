from selenium import webdriver
import unittest

class NewVisitortest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
        
    def test_can_write_an_invitation_and_retrieve_it_later(self):                
        # Zarko je cuo za novu web aplikaciju koja mu moze pomoci da organizuje 
        # svoje sportske aktivnosti. Otvara pocetnu stranicu da vidi o cemu se 
        # tu radi.
        self.browser.get('http://localhost:8000/')

        # Primjecuje da naslov stranice i zaglavlje spominju
        # sportskih aktivnosti.
        self.assertIn('sportske aktivnosti', self.browser.title)
        self.fail('Finish the test!')
        
        # Pozvan je da napise pozivnicu za svoju prvu aktivnost

        # Upisuju "Termin 10.01.! Hajmo prijave! :)" u text box 

        # Kada pritisne enter, stranica se azurira i prizuje se pozivnica
        # koju je upravo napisao "Termin 10.01.! Hajmo prijave! :)"

        # Tu se i dalje nalazi text box koji poziva da napise odgovor na pozivnicu
        # ili dodatni komentar. On upisuje "Žarko" da bi drugi znali da je on 
        # napisao pozivnicu.

        # Stranica se ponovo osvježava i sada se ispod postojeće poruke vidi drugi
        # komentar.

        # Žarko se pita da li ce aplikacija zapamtiti njegovu pozivnicu i da li ce
        # je moci poslati prijateljima na Facebook ili na mail. Tada primjecuje da
        # je aplikacija generisala jedinstveni URL za njegovu pozivnicu.

        # Posjecuje taj URL i primjecuje da su njegova pozivnica i komentar jos 
        # uvijek tamo.

        # Zadovoljan, odlazi na spavanje.

if __name__ == '__main__':
    unittest.main(warnings='ignore')


