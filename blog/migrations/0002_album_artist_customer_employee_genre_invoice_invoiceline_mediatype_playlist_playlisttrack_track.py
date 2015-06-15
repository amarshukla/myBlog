# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
            ],
            options={
                'db_table': 'Album',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
            ],
            options={
                'db_table': 'Artist',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'db_table': 'Customer',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
            ],
            options={
                'db_table': 'Employee',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
            ],
            options={
                'db_table': 'Genre',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
            ],
            options={
                'db_table': 'Invoice',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Invoiceline',
            fields=[
            ],
            options={
                'db_table': 'InvoiceLine',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mediatype',
            fields=[
            ],
            options={
                'db_table': 'MediaType',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
            ],
            options={
                'db_table': 'Playlist',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Playlisttrack',
            fields=[
            ],
            options={
                'db_table': 'PlaylistTrack',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
            ],
            options={
                'db_table': 'Track',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
