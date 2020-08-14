# Generated by Django 2.2.6 on 2020-08-14 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('comments', models.TextField()),
            ],
        ),
    ]
