# Generated by Django 2.0.6 on 2018-06-14 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subdomain',
            old_name='requester_id',
            new_name='requester_ids',
        ),
    ]
