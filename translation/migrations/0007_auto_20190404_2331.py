# Generated by Django 2.1.7 on 2019-04-04 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0006_auto_20190404_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='context_examples',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='translation',
            name='origin_text',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='translation',
            name='target_text',
            field=models.CharField(default='', max_length=250),
        ),
    ]
