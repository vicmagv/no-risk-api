# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20151207_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskproject',
            name='id_project',
            field=models.ForeignKey(related_name='RiskProjects', to='app.Project'),
        ),
    ]
