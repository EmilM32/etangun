# Generated by Django 2.2.7 on 2019-11-25 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eTangun', '0006_addresses_competitiondict_competitionresult'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addresses',
            old_name='comment',
            new_name='descr',
        ),
    ]