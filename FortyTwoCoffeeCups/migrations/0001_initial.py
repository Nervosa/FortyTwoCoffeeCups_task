# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PersonBio'
        db.create_table(u'FortyTwoCoffeeCups_personbio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('skype_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('jabber_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'FortyTwoCoffeeCups', ['PersonBio'])

    def backwards(self, orm):
        # Deleting model 'PersonBio'
        db.delete_table(u'FortyTwoCoffeeCups_personbio')

    models = {
        u'FortyTwoCoffeeCups.personbio': {
            'Meta': {'object_name': 'PersonBio'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['FortyTwoCoffeeCups']
