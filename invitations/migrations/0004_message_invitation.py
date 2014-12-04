# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0003_invitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='invitation',
            field=models.ForeignKey(to='invitations.Invitation', default=None),
            preserve_default=True,
        ),
    ]
