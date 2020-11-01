# Generated by Django 3.0.6 on 2020-10-26 08:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(max_length=255)),
                ('image', models.ImageField(default='', upload_to='media/image')),
                ('is_delete', models.SmallIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'f_update',
            },
        ),
    ]