# Generated by Django 4.1.7 on 2023-03-07 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='branchNDyear',
            new_name='branchNyear',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='waPhone',
            new_name='wanumber',
        ),
    ]
