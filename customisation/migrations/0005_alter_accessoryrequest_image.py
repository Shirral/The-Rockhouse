# Generated by Django 4.2 on 2024-12-10 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customisation', '0004_alter_accessoryrequest_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessoryrequest',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='accessory_requests/'),
        ),
    ]