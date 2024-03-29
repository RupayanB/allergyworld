# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant'
        db.create_table(u'allergyworld_restaurant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'allergyworld', ['Restaurant'])


    def backwards(self, orm):
        # Deleting model 'Restaurant'
        db.delete_table(u'allergyworld_restaurant')


    models = {
        u'allergyworld.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['allergyworld']