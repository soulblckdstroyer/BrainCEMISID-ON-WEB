# Generated by Django 3.0.2 on 2020-04-27 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesFromNeuron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('name_class', models.CharField(default='', max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images_collection', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
