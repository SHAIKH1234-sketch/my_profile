# Generated by Django 3.0.3 on 2021-08-30 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeTech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.CharField(max_length=50)),
                ('tachnology', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('side_show', models.CharField(max_length=5)),
                ('working_timeline', models.CharField(max_length=20)),
            ],
        ),
    ]