# Generated by Django 5.0.3 on 2024-04-01 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Notice',
        ),
    ]