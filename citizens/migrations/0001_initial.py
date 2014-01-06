# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Community'
        db.create_table(u'citizens_community', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'citizens', ['Community'])

        # Adding model 'User'
        db.create_table(u'citizens_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('postalCode', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'citizens', ['User'])

        # Adding M2M table for field community on 'User'
        m2m_table_name = db.shorten_name(u'citizens_user_community')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'citizens.user'], null=False)),
            ('community', models.ForeignKey(orm[u'citizens.community'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'community_id'])

        # Adding model 'Concern'
        db.create_table(u'citizens_concern', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('positiveVotes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('negativeVotes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['citizens.User'])),
        ))
        db.send_create_signal(u'citizens', ['Concern'])


    def backwards(self, orm):
        # Deleting model 'Community'
        db.delete_table(u'citizens_community')

        # Deleting model 'User'
        db.delete_table(u'citizens_user')

        # Removing M2M table for field community on 'User'
        db.delete_table(db.shorten_name(u'citizens_user_community'))

        # Deleting model 'Concern'
        db.delete_table(u'citizens_concern')


    models = {
        u'citizens.community': {
            'Meta': {'object_name': 'Community'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'citizens.concern': {
            'Meta': {'object_name': 'Concern'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['citizens.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'negativeVotes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'positiveVotes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'citizens.user': {
            'Meta': {'object_name': 'User'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'community': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['citizens.Community']", 'symmetrical': 'False'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'postalCode': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['citizens']