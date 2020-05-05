# Generated by Django 3.0.5 on 2020-05-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getdata', '0002_all_building'),
    ]

    operations = [
        migrations.RenameField(
            model_name='all',
            old_name='electric',
            new_name='meas',
        ),
        migrations.RemoveField(
            model_name='all',
            name='gas',
        ),
        migrations.RemoveField(
            model_name='all',
            name='water',
        ),
        migrations.AddField(
            model_name='all',
            name='util',
            field=models.CharField(default='0', max_length=50),
            preserve_default=False,
        ),
    ]
