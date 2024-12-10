# Generated by Django 4.2 on 2024-12-10 22:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customisation', '0002_alter_accessories_rock_shape'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoryRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('colour', models.CharField(blank=True, max_length=50, null=True)),
                ('type', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=models.SET(None), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
