# Generated by Django 2.2.19 on 2022-10-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseformapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseform',
            name='module_file',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='courseform',
            name='subject_file',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='courseform',
            name='topic_file',
            field=models.FileField(upload_to=''),
        ),
    ]
