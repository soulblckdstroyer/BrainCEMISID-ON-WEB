# Generated by Django 2.2.5 on 2019-11-09 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hearing_network', '0002_auto_20191109_0821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rbfneuron',
            old_name='_has_knowledge',
            new_name='has_knowledge',
        ),
    ]