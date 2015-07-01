# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_album_artist_customer_employee_genre_invoice_invoiceline_mediatype_playlist_playlisttrack_track'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='Invoiceline',
        ),
        migrations.DeleteModel(
            name='Mediatype',
        ),
        migrations.DeleteModel(
            name='Playlist',
        ),
        migrations.DeleteModel(
            name='Playlisttrack',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]
