from django.test import TestCase
from FortyTwoCoffeeCups.models import PersonBio
from django.core.urlresolvers import reverse

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