# Generated by Django 2.0.1 on 2018-03-01 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180301_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='mines_placed',
            field=models.BooleanField(default=False),
        ),
    ]