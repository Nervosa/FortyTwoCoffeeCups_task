# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PersonBio.photo'
        db.add_column(u'FortyTwoCoffeeCups_personbio', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PersonBio.photo'
        db.delete_column(u'FortyTwoCoffeeCups_personbio', 'photo')


    models = {
        u'FortyTwoCoffeeCups.http_request_for_db': {
            'Meta': {'object_name': 'Http_Request_for_DB'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other_info': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'server_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'server_port': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'FortyTwoCoffeeCups.personbio': {
            'Meta': {'object_name': 'PersonBio'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skype_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['FortyTwoCoffeeCups']