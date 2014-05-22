# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        Man = orm['man.man']
        for man in Man.objects.filter(follow_ids__isnull=False):
            follow_mans = man.follow_ids.split()
            for man_f in follow_mans:
                man.follow_mans.add(Man.objects.get(id=man_f))

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'man.man': {
            'Meta': {'object_name': 'Man'},
            'follow_ids': ('django.db.models.fields.TextField', [], {}),
            'follow_mans': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'follow_mans_rel_+'", 'to': u"orm['man.Man']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['man']
    symmetrical = True
