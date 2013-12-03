from django.template import Template, Context
from django.test import TestCase
from FortyTwoCoffeeCups.models import PersonBio, Http_Request_for_DB
from django.core.urlresolvers import reverse
from django.test import Client


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
        c = Client(SERVER_NAME='GetBarista.com')
        response = c.post('/')
        self.assertEqual(response.status_code, 200)
        test_request = Http_Request_for_DB.objects.all().filter(server_name='GetBarista.com')
        self.assertEqual(test_request[0].id, 1)

    def test_custom_context_processor(self):
        t = Template('{% if all_settings.DEBUG %}WE ARE USING DEBUG MODE{% else %}WE DO NOT USE DEBUG MODE{% endif %}')
        c = Context({})
        try:
            self.assertEqual(t.render(c), 'WE ARE USING DEBUG MODE')
        except:
            self.assertEqual(t.render(c), 'WE DO NOT USE DEBUG MODE')