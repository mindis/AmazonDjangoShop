# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.search_index'
        db.add_column('shop_category', 'search_index',
                      self.gf('django.db.models.fields.IntegerField')(default=7),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.search_index'
        db.delete_column('shop_category', 'search_index')


    models = {
        'shop.category': {
            'Meta': {'object_name': 'Category'},
            'amazon_node_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'search_index': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'asin': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'large_image': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'medium_image': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'popularity': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'shop.staticpage': {
            'Meta': {'object_name': 'StaticPage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['shop']