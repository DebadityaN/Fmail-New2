# Generated by Django 5.0 on 2023-12-30 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmail', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='detail',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
