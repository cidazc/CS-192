# Generated by Django 2.1.7 on 2019-04-04 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0005_auto_20190308_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='translation',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]