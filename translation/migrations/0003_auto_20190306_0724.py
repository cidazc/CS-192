# Generated by Django 2.1.5 on 2019-03-06 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0002_delete_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TranslationMod',
            new_name='Translation',
        ),
    ]