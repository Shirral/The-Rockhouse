# Generated by Django 4.2 on 2024-11-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rock',
            name='short_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
