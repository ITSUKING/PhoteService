# Generated by Django 2.2.7 on 2019-11-28 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Category'),
            preserve_default=False,
        ),
    ]
