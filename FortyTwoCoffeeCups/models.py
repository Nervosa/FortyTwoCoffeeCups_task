from django.db import models


class PersonBio(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField(verbose_name="Date of birth")
    bio = models.TextField(verbose_name="Bio of a person")
    email = models.EmailField()
    skype_id = models.CharField(max_length=50)
    jabber_id = models.CharField(max_length=50)
    other_contacts = models.TextField(verbose_name="Other contacts")

    def __unicode__(self):
        return self.name + " " + self.surname

    class Meta:
        ordering = ['id']


class Http_Request_for_DB(models.Model):

    server_name = models.CharField(max_length=100)
    server_port = models.CharField(max_length=15)
    other_info = models.CharField(max_length=5000)