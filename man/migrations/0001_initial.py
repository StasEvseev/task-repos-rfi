# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Man'
        db.create_table(u'man_man', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('follow_ids', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'man', ['Man'])


    def backwards(self, orm):
        # Deleting model 'Man'
        db.delete_table(u'man_man')


    models = {
        u'man.man': {
            'Meta': {'object_name': 'Man'},
            'follow_ids': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['man']