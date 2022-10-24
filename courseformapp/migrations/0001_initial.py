# Generated by Django 2.2.19 on 2022-10-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('couse_unique_id', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=255)),
                ('is_old_curriculam', models.BooleanField(default=False)),
                ('subject_file', models.FileField(upload_to='subfiles')),
                ('module_file', models.FileField(upload_to='modulefiles')),
                ('topic_file', models.FileField(upload_to='topicfiles')),
            ],
        ),
    ]