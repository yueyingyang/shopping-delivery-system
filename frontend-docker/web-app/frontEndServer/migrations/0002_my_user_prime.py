# Generated by Django 3.0.2 on 2020-04-23 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontEndServer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_user',
            name='prime',
            field=models.BooleanField(default=False),
        ),
    ]
