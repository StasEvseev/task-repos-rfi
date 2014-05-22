# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field follow_mans on 'Man'
        m2m_table_name = db.shorten_name(u'man_man_follow_mans')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_man', models.ForeignKey(orm[u'man.man'], null=False)),
            ('to_man', models.ForeignKey(orm[u'man.man'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_man_id', 'to_man_id'])


    def backwards(self, orm):
        # Removing M2M table for field follow_mans on 'Man'
        db.delete_table(db.shorten_name(u'man_man_follow_mans'))


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