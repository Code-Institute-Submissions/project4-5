# Generated by Django 2.2.6 on 2020-08-15 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20200814_0951'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feedback',
            new_name='Comment',
        ),
    ]
