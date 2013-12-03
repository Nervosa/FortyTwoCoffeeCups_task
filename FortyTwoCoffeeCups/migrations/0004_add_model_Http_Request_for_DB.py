# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Http_Request_for_DB'
        db.create_table(u'FortyTwoCoffeeCups_http_request_for_db', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('server_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('server_port', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('other_info', self.gf('django.db.models.fields.CharField')(max_length=5000)),
        ))
        db.send_create_signal(u'FortyTwoCoffeeCups', ['Http_Request_for_DB'])

    def backwards(self, orm):
        # Deleting model 'Http_Request_for_DB'
        db.delete_table(u'FortyTwoCoffeeCups_http_request_for_db')

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
            'skype_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['FortyTwoCoffeeCups']
