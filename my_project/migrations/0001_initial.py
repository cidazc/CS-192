# Generated by Django 2.1.5 on 2019-02-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_language', models.CharField(max_length=250)),
                ('target_language', models.CharField(max_length=250)),
                ('origin_text', models.CharField(max_length=250)),
                ('target_text', models.CharField(max_length=250)),
                ('context_examples', models.CharField(max_length=500)),
                ('upvotes', models.IntegerField()),
                ('downvotes', models.IntegerField()),
            ],
        ),
    ]
