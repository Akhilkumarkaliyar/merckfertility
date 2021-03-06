# Generated by Django 3.1.1 on 2020-10-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='f_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nurseid', models.CharField(blank=True, max_length=100, null=True)),
                ('accesscode', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('hospital', models.CharField(max_length=50)),
                ('speciality', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
