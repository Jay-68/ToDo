# Generated by Django 2.2 on 2020-01-03 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='completed',
            new_name='complete',
        ),
    ]
