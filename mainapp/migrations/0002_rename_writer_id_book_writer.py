# Generated by Django 4.1 on 2022-11-11 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='writer_id',
            new_name='writer',
        ),
    ]
