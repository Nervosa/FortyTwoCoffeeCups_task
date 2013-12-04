from django.test import TestCase
from FortyTwoCoffeeCups.models import PersonBio, Http_Request_for_DB
from django.core.urlresolvers import reverse
from django.test import Client
import string


class PersonBioTest(TestCase):

    def test_homepage(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No BIOs available.')
        new_bio = PersonBio(name='Test Name',
                            surname='Test Surname',
                            date_of_birth='2000-01-01',
                            bio='Test Bio',
                            email='TestEmail@test.com',
                            skype_id='TestSkype',
                            jabber_id='TestJabber@jabber.co',
                            other_contacts='Test Other Contacts')
        new_bio.save()
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TestJabber@jabber.co')

    def test_custom_middleware(self):
        url = reverse("home")
        c = Client(SERVER_NAME='GetBarista.com')
        response = c.post(url)
        self.assertEqual(response.status_code, 200)
        test_request = Http_Request_for_DB.objects.all().filter(server_name='GetBarista.com')
        self.assertEqual(test_request[0].id, 1)

        url = reverse("requests")
        for i in range(0,5):
            response = c.post(url) # making POST request 5 times
        occurences = string.count(str(response.__dict__), 'GetBarista.com')

        self.assertEqual(occurences, 5) # totally 5 occurences should we have on a page displaying requests

        for i in range(0,50):
            response = c.post(url) # now making POST request 50 times
        occurences = string.count(str(response.__dict__), 'GetBarista.com')

        self.assertEqual(occurences, 10) # but the maximum of shown requests reached so there are only 10