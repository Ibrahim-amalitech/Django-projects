# Generated by Django 3.2 on 2021-04-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='accessible',
            field=models.BooleanField(default=False),
        ),
    ]
